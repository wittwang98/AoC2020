summation = 2020
inputs = []
split_index = 0
line = 123

file1 = open('input.txt', 'r') 

line = file1.readline()

while line:
    inputs.append(int(line.split('\n')[0]))
    line = file1.readline()
    
file1.close()

inputs.sort()

for a in range(len(inputs)):
    if inputs[a] >= (summation/2):
        split_index = a
        break
                
"""for b in range(split_index-1):  del 1
    for c in range(split_index, len(inputs)):
        if (inputs[b]+inputs[c]) == summation:
            print inputs[b]*inputs[c]
            break"""
    
for b in range(len(inputs)): #del 2
    for c in range(len(inputs)):
        for d in range(len(inputs)):
            if inputs[b] + inputs[c] + inputs [d] == summation:
                print(inputs[b] * inputs[c] * inputs [d])
                break