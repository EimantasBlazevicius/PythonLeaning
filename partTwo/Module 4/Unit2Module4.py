#This program will import and open a file
#will append additional data to the file and then display file information from the file in a formed fashion.

#append the file with Rio information, and read the heading information
wFile = open('main_temp.txt', 'a+')
wFile.write("Rio de Janeiro, Brazil, 30.0, 18.0\n")
wFile.seek(0)
headingsVar = wFile.readline()
wFile.close()
#setup values
firstLineLen = len(headingsVar)   #variable to know how much values should be skipped whist readin the entire file
headings = headingsVar.split(",")
lines = []
#read the lines
rFile = open('main_temp.txt', 'r')
rFile.seek(firstLineLen)
for var in rFile.readlines():
    lines.append(var.split(','))
rFile.close()
#print the lines
for line in lines:
    print(headings[0].capitalize() + " of " + line[0] + " " + headings[2] + " " + line[2] + " Celcius")



