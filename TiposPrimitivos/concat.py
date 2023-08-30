dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

two = list(dic2)
twoValues = list(dic2.values())
three = list(dic3)
threeValues = list(dic3.values())

for i in range(len(two)):
    dic1[two[i]] = twoValues[i]

for i in range(len(three)):
    dic1[three[i]] = threeValues[i]

print(dic1)

