getinput = input("Do you want to store a new record? (y/n) ")
#
# this is to remove any extra whitespace
getinput = getinput.strip()
#
# this is to convert all input to lower case
getinput = getinput.lower()
#
#read input value and create a record
if ("y" in getinput):
    readvaluename = input("Enter the Name: ") 
    readvalueage = input("Enter the Age: ")
    readvaluelocation = input("Enter the Location: ")
    tmpvariable = readvaluename+","+readvalueage+","+readvaluelocation+"\n"
#
# open a record file myrecord.csv in write mode and write the record and close it
    fopen=open("myrecord.csv","w")
    fopen.write(tmpvariable)
    fopen.close()
    