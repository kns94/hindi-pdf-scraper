#Social Cops task 2.0 - To scrape a pdf file and to get database of voters in Faizlabad district
#Kushal Shah

import numpy as np
import sys

database=np.empty((4,5),dtype=object) #Numpy Array - Triplets

inputfile=sys.argv[1] #Input File

line_count=1

database[0,0]="Name"				#Header - Name
database[0,1]="Father's Name/Husband's Name"	#
database[0,2]="Count"				#
database[0,3]="Age"				#
database[0,4]="Gender"				#

count=1

tokens=[]
for line in open(inputfile,'r'):

	tokens[:]=[]

	line=line.strip().split(',')		#Removing , 

	for char in line:
		if(bool(char)):
			tokens.append(char)	#Removing blank spaces

	#token=tokens.strip().split(':')

	if((line_count%6)==1):

		#for token in tokens:
		#	print(token.decode('utf-8','ignore'))

		tok=tokens[0].strip().split(':')
		tok1=tokens[1].strip().split(':')
		tok2=tokens[2].strip().split(':')

		database[count,0] = unicode(tok[1], "utf-8", errors="ignore")		#First Name  
		database[count+1,0] = unicode(tok1[1], "utf-8", errors="ignore")	#Second Name 
		database[count+2,0] = unicode(tok2[1], "utf-8", errors="ignore")	#Third Name
		
		#line_count=line_count+1
		#print(line_count)
		pass

	if((line_count%6)==2):

		#for token in tokens:
		#	print(token.decode('utf-8','ignore'))

		#print(line_count)

		tok=tokens[0].strip().split(':')
		tok1=tokens[1].strip().split(':')
		tok2=tokens[2].strip().split(':')

		database[count,1] = unicode(tok[1], "utf-8", errors="ignore")		#First person's father's/husband's name
		database[count+1,1] = unicode(tok1[1], "utf-8", errors="ignore")	#Second person's father's/husband's name
		database[count+2,1] = unicode(tok2[1], "utf-8", errors="ignore")	#Third person's father's/husband's name

		#line_count=line_count+1
		#print(line_count)
		pass

	if((line_count%6)==3):

		tok=tokens[0].strip().split(':')
		tok1=tokens[1].strip().split(':')
		tok2=tokens[2].strip().split(':')

		database[count,2] = unicode(tok[1], "utf-8", errors="ignore")		#First person's count (Sankhya)
		database[count+1,2] = unicode(tok1[1], "utf-8", errors="ignore")	#Second person's count (Sankhya)
		database[count+2,2] = unicode(tok2[1], "utf-8", errors="ignore")	#Third person's count (Sankhya)

		#print(line_count)
		#line_count=line_count+1
		pass

	if((line_count%6)==4):

		database[count,3]=tokens[1].decode('utf-8')		#First person's age
		database[count+1,3]=tokens[4].decode('utf-8')		#Second person's age
		database[count+2,3]=tokens[7].decode('utf-8')		#Third person's age

		#line_count=line_count+1

		#for token in tokens:
		#	print(token.decode('utf-8','ignore'))

		tok=tokens[2].strip().split(':')
		tok1=tokens[5].strip().split(':')
		tok2=tokens[8].strip().split(':')

		database[count,4] = unicode(tok[1], "utf-8", errors="ignore")		#First person's gender
		database[count+1,4] = unicode(tok1[1], "utf-8", errors="ignore")	#Second person's gender
		database[count+2,4] = unicode(tok2[1], "utf-8", errors="ignore")	#Third person's gender
		
		temp=np.empty((3,5),dtype=object) #Numpy Array - Triplets
		database=np.concatenate((database,temp))
		count=count+3

		#print("\n\n")
		#print(line_count)


	if((line_count%6)==5):
		#line_count=line_count+1
		pass

	if((line_count%6)==0):
		pass


	line_count=line_count+1

#print(database)

i=0

out=open(sys.argv[2],'w')

while(i<count):
	j=0
	while(j<5):
		if(bool(database[i][j])):	
			out.write(str(database[i][j].encode("utf-8")))
		out.write(",")
		j=j+1
	out.write("\n")
	i=i+1
