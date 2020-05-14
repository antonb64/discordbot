f = open("mods")
l2 = f.readlines()
l = []
for i in l2:
    l.append(int(i))
print(l)
f.close()