import subprocess
import matplotlib.pyplot as plt
import matplotlib.ticker

AES = []
XChaCha20 = []
trials = []
for i in range(1000):
    # runs command like `node filename.js input`
    a = subprocess.run(['node', 'D:\GitHub\MQTT-Payload-Encryption\Decryption\AES.js',
                        'eyJkYXRhIjpbIlBscitxREFLcit4WUJ5Q2NTYkVIQTYyWnBBR2dDd3RhZm1qRlk0M3l0MVUrdkJrSHJJYmJ3RjgxNUIvV3lZUThEUXhvQ2k5WldXNUcwRE1qQWUvMHdRRWdYOUxxU3lkVXV5ZExiMzFJRjU0PSIsIlFVSkRSRVZHUjBGQ1EwUkZSa2RCUWc9PSJdfQ=='],
                       capture_output=True, text=True).stdout.strip(
        "this is a longer message being tested abcdefghijklmnopqrstuvwxyz\n")  # strips the plaintext output to read numberical data only
    c = subprocess.run(['node', 'D:\GitHub\MQTT-Payload-Encryption\Decryption\XChaCha20.js',
                        'eyJkYXRhIjpbImN4WHU3Ym92bEo3dEZHbEY2aUpHUytpenp4RmVxaWV4Z1BVK0pVaXAiLCJCY3JFeDJpUVA3dVZFRHlCNFRpSk1pckRTM05QWnJmdyJdfQ=='],
                       capture_output=True, text=True).stdout.strip(
        "this is a longer message being tested abcdefghijklmnopqrstuvwxyz\n")  # strips the plaintext output to read numberical data only

    AES.append(a)
    XChaCha20.append(c)
    trials.append(i)


def Average(lst):
    return sum(lst) / len(lst)


AES = [float(i) / 1000000 for i in AES]
XChaCha20 = [float(i) / 1000000 for i in XChaCha20]

print(XChaCha20)
print(AES)

print("Average XChaCha" + str(Average(XChaCha20)))
print("Average AES" + str(Average(AES)))

# generates plot
plt.rcParams["figure.figsize"] = [6.50, 3.50]
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots()
ax.scatter(trials, XChaCha20, color="black", label='Execution Time: XChaCha20', s=2)
ax.scatter(trials, AES, color="orange", label="Execution Time: AES", s=2)
ax.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter("{x:.4f}"))
plt.title("Performance Test Comparison", fontsize=12)
plt.plot(trials, [Average(XChaCha20) for x in XChaCha20], color="brown", label='Average Time: XChaCha20', linestyle='--')
plt.plot(trials, [Average(AES) for x in AES], color="red", label='Average Time: AES', linestyle='--')
plt.xlabel("Order of Trials", fontsize=9)
plt.ylabel("Time (ms)", fontsize=9)
plt.ylim(10.5,14.5)
plt.legend(loc='upper left', prop={'size': 6})
plt.show()

# plt.savefig('foo.png',edgecolor='RED',transparent=False)
