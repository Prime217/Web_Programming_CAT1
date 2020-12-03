def csc_217_Seperated():
    searchfile = open("CSC_217_attendance_ week1final.txt", "r")
    b =[i for i in searchfile if "B135" in i]
    print (b)
    searchfile.close()
    file=open("CSC_217_Computer.txt","w")
    for j in b:
        file.write(j+"\n")
    file.close()

    searchfile = open("CSC_217_attendance_ week1final.txt", "r")
    b =[i for i in searchfile if "B141" in i]
    print (b)
    searchfile.close()
    file=open("CSC_217_IT.txt","w")
    for j in b:
        file.write(j+"\n")
    file.close()


csc_217_Seperated()


