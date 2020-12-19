data = []
file = open("input.txt", "r")
line = file.readline()

while line:
    data.append(line.split('\n')[0])
    line = file.readline()
    
file.close()

steps = [(1,1), (3,1), (5,1), (7,1), (1,2)]
encounters = []
for step in steps:
    trees = 0
    i = 0
    xpos = 0
    while i < len(data):
        a = data[i]
        if a[xpos%len(a)] == "#":
            trees +=1
            
        xpos += step[0]
        i += step[1]
    encounters.append(trees)    

res = 1
for b in encounters:
    res = res*b
    
print(encounters, res)