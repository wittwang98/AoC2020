data = []

file = open("input.txt", "r")
line = file.readline()

while line:
    data.append(line.split('\n')[0])
    line = file.readline()
    
file.close()

xpos = 0
trees = 0
print(data)
for a in data:
    if a[xpos%len(a)] == "#":
        trees +=1
        
    xpos += 3
    
print(trees)