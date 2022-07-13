import subprocess
import matplotlib.pyplot as plt

numbers = []
trials = []
for i in range(1000):
    a = subprocess.run([r'C:\Program Files (x86)\Nodist\node.exe', r'C:\Users\shahm\OneDrive\Desktop\decrypt.js',
                        'eyJkYXRhIjpbIlBscitxREFLcit4WUJ5Q2NTYkVIQTYyWnBBR2dDd3RhZm1qRlk0M3l0MVUrdkJrSHJJYmJ3RjgxNUIvV3lZUThEUXhvQ2k5WldXNUcwRE1qQWUvMHdRRWdYOUxxU3lkVXV5ZExiMzFJRjU0PSIsIlFVSkRSRVZHUjBGQ1EwUkZSa2RCUWc9PSJdfQ=='],
                       capture_output=True, text=True).stdout.strip(
        "this is a longer message being tested abcdefghijklmnopqrstuvwxyz\ndefault:")
    numbers.append(a)
    trials.append(i)


def Average(lst):
    return sum(lst) / len(lst)


numbers = [int(float(i)) for i in numbers]
print(numbers)
print("average " + str(Average(numbers)))

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.title("Performance Test")
plt.plot(trials, numbers, color="lightblue", label='Execution Time')
plt.plot(trials, [sum(numbers) / len(numbers) for i in trials], color="green", label='Average', linestyle='--')
plt.xlabel("Order of Trials")
plt.ylabel("Time (ms)")
plt.legend(loc='upper left')
plt.show()
