import re
expanding =  0
f = open("text.nasm","r")import re
expanding =  0
f = open("text.nasm","r")
args = []
deftab = []
argtab = []
defination =[]
namtab = []
f = f.readlines()
deflist = []
arglist = []
macroRead = 0
singlelinedef = []
def argsdef(pos,args):
	s = deftab[pos]
	#print(s)
	x = 0
	#print(args[pos])
	for i in args[pos]:
		argtab.append(i)

	
	s = list(s)
	count = 0
	for n, i in enumerate(s):
		if i == "#":
			s[n] = "" 
			s[n+1] = argtab[pos][count]
			count = count+2
			
				
	s = "".join(s)			

	return s



def expand(nam,args):
	expanding = 1
	for i in namtab:
		if i == nam:
			pos = namtab.index(nam)		
	expandedMacro = argsdef(pos,args)
	processline(expandedMacro)
	
	 
def define(macroname , line):
	global macroRead
	namtab.append(macroname)
	pos = line.index(macroname)
	pos = pos+1
	for i in range(pos,len(line)):
		arglist.append("#" + line[i][1:2])
		
	
	macroRead = 1

#def getline(line):
			
		
def processline(line):                                
	line = re.sub(r';.*\n',"",line)
	line = line.strip()
	line=line+'\n'
	global macroRead
	global args 
	line = line.split(" ")
	#print(line)
	for word in line:
		flag=0
		for nam in namtab:
			if word == nam: 
				loc = line.index(word)
				args.append(list(line[(loc+1):len(line)]))
				expand(nam,args)
				flag=1
				
			
		if flag==1:
			break
		if word == "%macro":
			pos = line.index(word)	
			define(line[pos+1],line)
			
			break
			
		elif word == "%mend\n":
			macroRead =0
			defination = ' '.join(deflist)
			deftab.append(defination)
			deflist.clear()
		elif macroRead ==1:
			deflist.append(word)
		else:
			print(word,end=' ')	

	for word in line:
		if word == "%Sdef":
			loc = line.index(word)
			singlelinedef.append(line[loc+1])
			singlelinedef.append(line[loc+2])
		elif word in singlelinedef:
			print("yes")	


for i in f:
	#getline(i)
	processline(i)



	

print(singlelinedef)
#print(namtab)
#print(deftab)
#print(arglist)
#print(argtab)


