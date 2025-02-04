immortals = ["cf_0","patrick_1","exirly_2","steel_3","windvayne_4","rads_5","bunnypls_6","Fastnitro_7","fearfulwalker_8","surgeian_9","gloseph_10","tenshi_11"]

with open("rawscore", "r") as file:
    data = file.read().strip()  
poop = data.split(",")
rawscore = [int(num) for num in poop]

updList = []

for i in range(len(rawscore)):
    updList.append([immortals[i],rawscore[i]])

amt = int(input("How much?"))
ans = int(input("Who to update?"))
updList[ans] = [immortals[ans],rawscore[ans]+amt]
rawscore[ans] = rawscore[ans]+amt

retRaw = ""
for i in range(len(rawscore)):
    if i != len(rawscore)-1:
        retRaw = retRaw+str(rawscore[i])+","
    else:
        retRaw = retRaw+str(rawscore[i])

displayScore = str(updList)

with open("rawscore","w") as file:
    file.write(retRaw)
    
with open("logs.txt","w") as file:
    file.write(displayScore)