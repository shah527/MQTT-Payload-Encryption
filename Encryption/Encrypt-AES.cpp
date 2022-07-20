#include <ESP8266WiFi.h>  //WiFi
#include <PubSubClient.h> //MQTT
#include <AES.h>          //AES
#include <ebase64.h>      //base64
#include <ArduinoJson.h>  //JSON

StaticJsonDocument<256> doc;

JsonArray data = doc.createNestedArray("data"); // JSON array
char out[512];                                  // contains message to be sent to broker

const char *ssid = "lenovo";                 // WiFi name
const char *password = "espcheck";           // Password
const char *mqtt_broker = "149.162.184.124"; // Broker IP
const char *topic = "test";                  // MQTT topic
const char *message;
const int mqtt_port = 1883;
WiFiClient espClient;
PubSubClient client(espClient);

/********************************************************************/
void printArray(String name, byte *arr, int length) // function for printing array
{
    Serial.print(name + ": ");
    for (int i = 0; i < length; i++)
    {
        Serial.write(arr[i]);
    }
    Serial.println();
}

/********************************************************************/
void encryptAES() // function to get encrypted data
{
    byte key[] = {'m', 'y', 's', 'e', 'c', 'r', 'e', 't', 'p', 'a', 's', 's', 'w', 'o', 'r', 'd'}; // key, length 16
    String msg = "mahir sending msg from lenovo";                                                  // plaintext

    AES aes;

    // init vector, constant for testing simplicity, will be randomized for security later on
    byte iv[N_BLOCK] = {65, 66, 67, 68, 65, 66, 67, 68, 65, 66, 67, 68, 65, 66, 67, 68};
    // plain message in array of bytes
    byte plain[200];
    // encrypted message
    byte cipher[200];

    // BASE64 encoded data, to be sent to server
    char ivb64[200];
    char cipherb64[200];

    // set key
    aes.set_key(key, sizeof(key));

    // transform string to byte[]
    msg.getBytes(plain, sizeof(plain));
    printArray("Plain message", plain, msg.length());

    // BASE64 encode initialization vector (IV)
    byte ivb64len = base64_encode(ivb64, (char *)iv, N_BLOCK);
    printArray("IV", iv, 16);
    Serial.println("IV in B64: " + String(ivb64));

    // encrypt message with AES128 CBC pkcs7 padding w/ key and IV
    aes.do_aes_encrypt(plain, strlen((char *)plain), cipher, key, 128, iv);
    printArray("Encrypted message", cipher, aes.get_size());
    Serial.println("Encrypted message size: " + String(aes.get_size()));

    // BASE64 encode encrypted message
    byte cipherb64len = base64_encode(cipherb64, (char *)cipher, aes.get_size());
    Serial.println("Encrypted message in B64: " + String(cipherb64));

    aes.clean();

    Serial.println();
    Serial.println();

    data.add(cipherb64);
    data.add(ivb64);
    serializeJson(doc, out);
    /*added quotes around the message to be sent because it is passed to shell, and then to a decrypting program.
    The command prompt gets rid of the quotes inside the JSON array if they aren't escaped.*/

    String x = String(out);         // converts to string to add quotes
    String value = "\"" + x + "\""; // added quotes
    value.toCharArray(out, 512);    // converted back again to char to be send using MQTT
}

/********************************************************************/
void setup(void)
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
            Serial.println("MQTT broker connected");
        }
        else
        {
            Serial.print("Failed to connect. State is: ");
            Serial.print(client.state());
            delay(2000);
        }
    }
    encryptAES();               // encrypting function
    client.publish(topic, out); // publishes data to broker
}

/********************************************************************/
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

/********************************************************************/
void loop(void)
{
    client.loop();
}