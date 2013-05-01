import random
import os.path
import os
import datetime
import webbrowser
 
def rows(x):
	if os.path.exists("./" + file_name):
		os.remove("./" + file_name)
	for y in range(0,x,1):
		num = []
 
		for i in range(0,5,1):
			x  = random.randrange(1,46,1)
			if x in num:
				x  = random.randrange(1,46,1)
			num.append(x)
		
		jocker = random.randrange(1,21,1)
 
		name = str(num[0]) + " - " + str(num[1]) + " - " + str(num[2]) + " - " + str(num[3]) + " - " + str(num[4]) + " Joker: " + str(jocker)
 
		fileObj = open(file_name, "a")
		fileObj.write("γραμμη: " + str(y + 1) + "\n" + name + "\n")
		fileObj.close()
		print ("γραμμη: " + str(y + 1) + "\n" + name + "\n")
 
def check(n):
	if n > 0 and n <= 5:
		rows(int(n))
		s = input("το αρχειo θα σωθει σαν " + file_name + " θελεις να ανοιξει το αρχειο? (y/n) ")
		if s == "y":
			webbrowser.open(file_name)
		elif s == "n":
			print ("ενταξει γεια σου!!!")
		else:
			print ("What?")
	else:
		r = input("δωσε ποσες γραμμες θελεις [1-5]: ")
		recheck(r)
def recheck(n):
	check(int(n))
	
file_name = input("θελεις να δωσεις ονομα στο αρχειο? (ονομασια .txt) ή θελεις ονομασια ημερομηνια και ωρα πατωντας εντερ. ")
 
if file_name == "":
	now = datetime.datetime.now()
	file_name = now.strftime("%d-%m-%Y_%H:%M")
 
file_name = file_name + ".txt"	
r = input("δωσε ποσες γραμμες θελεις [1-5]: ")
		
check(int(r))
