

f = open("demo02.txt","w+")
f.write("This is line1")
f.close()


f = open("demo02.txt","w+")
for i in range(20):
    f.write("This is line %d\n"%(i+1))
f.close()


f = open("demo02.txt","a+")
for i in range(3):
    f.write("This is append line %d\n"%(i+1))
f.close()


f = open("demo02.txt","r")

con = f.read()

print(con)
f.close()


f = open("demo02.txt","r")

con = f.readline()

print(con)
f.close()

f = open("demo02.txt","r")

con = f.read(5)

print(con)
f.close()


f = open("demo02.txt","r")

con = f.read(10)
print(con)

print(f.tell())
print(f.seek(0))

con1 = f.read(20)
print(con1)

f.close()







