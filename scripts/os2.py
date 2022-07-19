#work in progress#


import subprocess
import matplotlib.pyplot as plt
import re
import matplotlib.ticker

numbersA = []
numbersC = []
numbersXC = []

trials = []
for i in range(1):
    a = subprocess.run(['node', r'C:\Users\shahm\OneDrive\Desktop\chachafinal.js',
                        'eyJkYXRhIjpbImN4WHU3Ym92bEo3dEZHbEY2aUpHUytpenp4RmVxaWV4Z1BVK0pVaXAiLCJCY3JFeDJpUVA3dVZFRHlCNFRpSk1pckRTM05QWnJmdyJdfQ=='],
                       capture_output=True, text=True).stdout.strip(
        "this is a longer message being tested abcdefghijklmnopqrstuvwxyz\n")
    b = subprocess.run([r'C:\Program Files (x86)\Nodist\node.exe', r'C:\Users\shahm\OneDrive\Desktop\decrypt.js',
                        'eyJkYXRhIjpbIlBscitxREFLcit4WUJ5Q2NTYkVIQTYyWnBBR2dDd3RhZm1qRlk0M3l0MVUrdkJrSHJJYmJ3RjgxNUIvV3lZUThEUXhvQ2k5WldXNUcwRE1qQWUvMHdRRWdYOUxxU3lkVXV5ZExiMzFJRjU0PSIsIlFVSkRSRVZHUjBGQ1EwUkZSa2RCUWc9PSJdfQ=='],
                       capture_output=True, text=True).stdout.strip(
        "this is a longer message being tested abcdefghijklmnopqrstuvwxyz\n")
    c = subprocess.run([r'C:\Program Files (x86)\Nodist\node.exe', r'C:\Users\shahm\OneDrive\Desktop\chacha20.js',
                        'eyJkYXRhIjpbInd2OGU1S2dUYyttSWx2WDlFQldrWlRWZVQ4ZldOQWIrZ0l0dXBjQmtVUE9FIiwiYVhaMWMyVmtabTl5ZEdWemRHbHVadz09Il19'],
                       capture_output=True, text=True).stdout.strip(
        "<Buffer 54 65 73 74 69 6e 67 20 75 73 69 6e 67 20 63 72 79 70 74 6f 20 6c 69 62 20 43 68 61 43 68 61 32 30>")
    numbersC.append(c)
    numbersA.append(b)
    numbersXC.append(a)

    trials.append(i)


def Average(lst):
    return sum(lst) / len(lst)
numbersA = [float(i) / 1000000 for i in numbersA]
numbersC = [float(re.sub('[n\n]', '', i)) / 1000000 for i in numbersC]
numbersXC = [float(i) / 1000000 for i in numbersXC]
print(numbersC)
print(numbersXC)
print(numbersA)
print("average ChaCha" + str(Average(numbersC)))
print("average XChaCha" + str(Average(numbersXC)))
print("average AES" + str(Average(numbersA)))

plt.rcParams["figure.figsize"] = [6.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig, ax = plt.subplots()


ax.scatter(trials, numbersC, color="blue", label='Execution Time: ChaCha20', s=2)
ax.scatter(trials, numbersXC, color="black", label='Execution Time: XChaCha20', s=2)
ax.scatter(trials, numbersA, color="orange", label="Execution Time: AES",s=2)
ax.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter("{x:.4f}"))
plt.title("Performance Test Comparison",fontsize = 12)
plt.plot(trials, [sum(numbersC) / len(numbersC) for i in trials], color="purple", label='Average Time: ChaCha20', linestyle='--')
plt.plot(trials, [sum(numbersXC) / len(numbersXC) for i in trials], color="brown", label='Average Time: XChaCha20', linestyle='--')
plt.plot(trials, [sum(numbersA) / len(numbersA) for i in trials], color="red", label='Average Time: AES', linestyle='--')


plt.xlabel("Order of Trials",fontsize = 9)

plt.ylabel("Time (ms)",fontsize = 9)

plt.legend(loc='upper left',prop={'size': 6})
plt.show()
#plt.savefig('foo.png',edgecolor='RED',transparent=False)
