file = open("sample.txt", "w")
file.write("dsp\n")

lines = ["devi\n", "D.O.B-7-10-2006\n", "College - MVGR\n"]
file.writelines(lines)

file.close()

file = open("sample.txt", "r")
print("read()\n:")
print(file.read())     
file.close()

file = open("sample.txt", "r")
print("\nreadline()\n:")
print(file.readline()) 
print(file.readline()) 
file.close()

file = open("sample.txt", "r")
print("\nreadlines():")
print(file.readlines()) 
file.close()
