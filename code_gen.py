import string, random, datetime

alphabet = string.ascii_letters + string.digits
codeLen = 12
numCodes = 30

codeList = []
#newCodeList = []

try :
	f = open("codelist.txt", "r")
	for line in f:
		codeList.append(line)
	f.close()
except Exception:
	pass	

f = open("codelist.txt", "a")

now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
f_new = open("newcodelist" + "_" + now  + ".txt", "w+")

i = 0
while (i < numCodes):
	code = ""
	for j in range(codeLen):
 		code = code + random.choice(alphabet)
 	if code not in codeList :
 		codeList.append(code)
 		#newCodeList.append(code)
 		f.write(code + "\n")
 		f_new.write(code + "\n")
 		i += 1

f.close()
f_new.close()

#print newCodeList


