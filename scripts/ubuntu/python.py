import subprocess


numbers = []
trials = []
for i in range(1000):
    a = subprocess.run([r'/home/ubuntu/.nvm/versions/node/v18.6.0/bin/node', r'/home/ubuntu/Downloads/scripts/ChaCha20.js',
                        'eyJkYXRhIjpbInd2OGU1S2dUYyttSWx2WDlFQldrWlRWZVQ4ZldOQWIrZ0l0dXBjQmtVUE9FIiwiYVhaMWMyVmtabTl5ZEdWemRHbHVadz09Il19'],
                       capture_output=True, text=True).stdout.strip(
        "Testing using crypto lib ChaCha20\n")
    numbers.append(a)
    trials.append(i)


def Average(lst):
    return sum(lst) / len(lst)


numbers = [float(i) / 1000000 for i in numbers]
print("ChaCha20 Data: \n\n")
print(numbers)
print("average " + str(Average(numbers)))

