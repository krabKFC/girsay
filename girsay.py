giraffe_head = ['   /)ii/)', ' (o  " )']
giraffe_neck = ['    | |', '    |o|']
giraffe_body = ['    | |_______||', '    |   o      |', '    | o  ___ o_|',
    '    || ||   || ||', '    || ||   || ||']
text = input("Text message: ")
num = int(input("Neck size: "))
z = 0

print("\n\n" + " " + "_" * len(text))
print("<" + text + ">")
print(" " + "‾" * len(text) + "\n")

for i in range(len(giraffe_head)):
    print(giraffe_head[i])

while z != num:
    if z % 2 == 0:
        print(giraffe_neck[0])
    else:
        print(giraffe_neck[1])
    z += 1

for x in range(len(giraffe_body)):
    print(giraffe_body[x])
