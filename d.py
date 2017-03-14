import csv
import re
in_file = open("output.csv", "rb")
reader = csv.reader(in_file)
out_file = open("dummy.csv", "wb")
writer = csv.writer(out_file)
for row in reader:
	#row[3] = 4
	wordlist = re.sub("[^\w!@?(-)+""\;><:*/.']", " " , row[5])
	if "document omitted" in wordlist or "image omitted" in wordlist or "vCard omitted" in wordlist or "added" in wordlist or "video omitted" in wordlist or "changed to" in wordlist or "audio omitted"  in wordlist or "created this group" in wordlist or "Messages you send to this group are now secured with end to end encryption" in wordlist:
		i=1
	else:
		row[5] = wordlist
		writer.writerow(row)
	
in_file.close()    
out_file.close()
