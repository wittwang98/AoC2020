import re
inputs = []
OKPW = 0;

file1 = open('input2.txt', 'r') 

line = file1.readline()

while line:
    temp= line.split('\n')[0]
    inputs.append(re.split(' |, |:|, |-|', temp))
    line = file1.readline()    
file1.close()

"""for a in inputs:   PART 1
    counter = 0
    for b in a[4]:
        if b == a[2]:
            counter += 1
    if (counter <= int(a[1])) and (counter >= int(a[0])):
        OKPW += 1"""

for a in inputs:   #PART 2
    if (a[4][int(a[0])-1] == a[2]) != (a[4][int(a[1])-1] == a[2]):
        OKPW += 1
        
print(OKPW)