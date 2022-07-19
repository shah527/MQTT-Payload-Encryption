import subprocess


numbers = []
trials = []
for i in range(1000):
    a = subprocess.run([r'/home/ubuntu/.nvm/versions/node/v18.6.0/bin/node', r'/home/ubuntu/Downloads/scripts/AES.js',
                        'eyJkYXRhIjpbIlBscitxREFLcit4WUJ5Q2NTYkVIQTYyWnBBR2dDd3RhZm1qRlk0M3l0MVUrdkJrSHJJYmJ3RjgxNUIvV3lZUThEUXhvQ2k5WldXNUcwRE1qQWUvMHdRRWdYOUxxU3lkVXV5ZExiMzFJRjU0PSIsIlFVSkRSRVZHUjBGQ1EwUkZSa2RCUWc9PSJdfQ=='],
                       capture_output=True, text=True).stdout.strip(
        "this is a longer message being tested abcdefghijklmnopqrstuvwxyz\n")
    numbers.append(a)
    trials.append(i)


def Average(lst):
    return sum(lst) / len(lst)


numbers = [float(i) / 1000000 for i in numbers]
print("AES Data \n\n")
print(numbers)
print("average " + str(Average(numbers)))

