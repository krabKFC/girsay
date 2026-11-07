giraffe_head = ['   /)ii/)', ' (o  " )']
giraffe_neck = ['    | |', '    |o|']
giraffe_body = ['    | |_______||', '    |   o      |', '    | o  ___ o_|',
    '    || ||   || ||', '    || ||   || ||']
text = input()

print(text)
for i in range(len(giraffe_head)):
    print(giraffe_head[i])
for z in range(len(giraffe_neck)):
    print(giraffe_neck[z])
for x in range(len(giraffe_body)):
    print(giraffe_body[x])
