#include <ESP8266WiFi.h>      //WiFi
#include <PubSubClient.h>     // MQTT
#include <ChaChaPolyHelper.h> //ChaChaPoly helper library https://github.com/dmaixner/esp8266-chachapoly
#include <ArduinoJson.h>      //JSON

StaticJsonDocument<256> doc;

const char *ssid = "lenovo";                 // WiFi name
const char *password = "espcheck";           // WiFi password
const char *mqtt_broker = "149.162.184.124"; // MQTT broker ip
const char *topic = "test";                  // MQTT topic
const char *message;
const int mqtt_port = 1883;
WiFiClient espClient;
PubSubClient client(espClient);

void setup()
{
    Serial.begin(115200);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to the WiFi network");
    client.setServer(mqtt_broker, mqtt_port);
    client.setCallback(callback);

    while (!client.connected())
    {
        String client_id = "esp8266-client-";
        client_id += String(WiFi.macAddress());
        Serial.printf("The client %s connects to mosquitto mqtt broker\n", client_id.c_str());

        if (client.connect(client_id.c_str()))
        {
            Serial.println("Connected to MQTT broker!");
        }
        else
        {
            Serial.print("Failed to connect, state is:");
            Serial.print(client.state());
            delay(2000);
        }
    }

    // key
    byte key[CHA_CHA_POLY_KEY_SIZE] = {
        0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
        0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18,
        0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28,
        0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38};
    // authentication
    byte auth[CHA_CHA_POLY_AUTH_SIZE] = {
        0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
        0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18};
    // initialization vector (IV)
    byte iv[CHA_CHA_POLY_IV_SIZE];
    ChaChaPolyCipher.generateIv(iv);

    // plain text message
    byte plainText[CHA_CHA_POLY_MESSAGE_SIZE];
    String plain = "sending message from lenovo";
    plain.getBytes(plainText, CHA_CHA_POLY_MESSAGE_SIZE);

    // encrypt plaintext
    byte cipherText[CHA_CHA_POLY_MESSAGE_SIZE];
    byte tag[CHA_CHA_POLY_TAG_SIZE];
    ChaChaPolyCipher.encrypt(key, iv, auth, plainText, cipherText, tag);
    byte text[CHA_CHA_POLY_MESSAGE_SIZE];
    // decrypting, to verify everything works
    ChaChaPolyCipher.decrypt(key, iv, auth, cipherText, text, tag);
    char *txt = (char *)text; // txt stores the decrypted message
    Serial.print(txt);        // to verify decrypted text matches initial plaintext

    // create json array that's being sent
    JsonArray data = doc.createNestedArray("data");
    data.add(cipherText);
    data.add(tag);
    data.add(iv);
    char out[512];
    serializeJson(doc, out);

    client.publish(topic, out); // Publish MQTT msg
}

void callback(char *topic, byte *payload, unsigned int length)
{
    Serial.print("Message arrived in topic: ");
    Serial.println(topic);
    Serial.print("Message:");

    for (int i = 0; i < length; i++)
    {
        Serial.print((char)payload[i]);
    }

    Serial.println();
    Serial.println(" - - - - - - - - - - - -");
}

void loop()
{
    client.loop();
}