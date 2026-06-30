'''f = open("D:\NEW CODE 2026\python\A.text", "r")
print(f.readlines())'''
#handling 
'''
try:
    f = open("D:\\NEW CODE 2026\\python\\b.txt", "r")
     
    print(f.readlines())
except:
    print("file not available ....! plz create file ")

else:
    f.close()
    print("File closed")

'''
    #copy 
try:
    with open ("D:\NEW CODE 2026\python\A.text/A.text") as f2:
        with open ("D:\NEW CODE 2026\python\A.text/B.text") as f3 :
             for i in f2:
                 f3.write(i)
except:
     print("file not available ....! plz create file ")
else:
    f2.close()
    print("File closed")