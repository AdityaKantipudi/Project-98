def swapfiledata():
    file1=input("Enter file 1 name.")
    file2=input("Enter file 2 name.")

    with open(file1,"r") as a:
        dataa=a.read()
    
    with open(file2,"r") as b:
        datab=b.read()
    
    with open(file1,"w") as p:
        p.write(datab)

    with open(file2,"w") as q:
        q.write(dataa)

swapfiledata()