file = open("teams.txt","rt")
team = "nonempty"
while (team != ""):
   team = file.readline()
   if (team != ""): print (team[:-1])   #get rid of extra newline character
   #print(len(team))
   #print(team[2:])
file.close()
#-------------------------------------------------------------------------------------------------------------------
list=['α','β','g','e'] #list = ['florida','clemson','duke']
list.append('114')
#print ('αυτη ειναι η λιστα:',list)
print()
file=open ('teams.txt','a')
for j in list:
    file.write(j)
file.write('\n')       #for j in list:file.write(j+'\n')->ta grafei katakoryfa sto arxeio
file.close()

#file = open("teams.txt","rt")
#team = file.readlines()
#print(team)
#print()
#print(team[35:])
#file.close()
