print('======Sample01')
# Open a file
fo = open("Sample.txt", "wb")
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)

print('====>Closing File Handling')
fo.close()
print("Closed or not : ", fo.closed)

print('====Writing to a file')
fo = open("Sample.txt", "w")
fo.write("Anil Loves Switching")
fo.close()


print('=====>Reading a file content')
fo = open('Sample.txt', 'r+')
f_read = fo.read(10)
f_read2 = fo.read(20)
fo.close()
print('File has: ', f_read)
fo = open('Sample.txt', 'r+')
f_read2 = fo.read(20)

print('File has: ', f_read2)


print('File Position is: ', fo.tell())
fo.close()




