# 실습 1

file_fath = open("C:/pyfile/gugudan.txt","w")

for i in range(2, 10):
    for j in range(1, 10):
        file_fath.write(f"{i} x {j} = {i * j}"+"\n")

file_fath.close()

file_fath = open("C:/pyfile/gugudan.txt","r")
data=file_fath.read()

print(data)

