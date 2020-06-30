import random,string
"""随机数练习"""
def create_str(num_int=0,num_letters=0,num_zh=0,num_pun=0):
    list = []
    for i in range(num_int):
        list.append(random.choice(string.digits))
    for i in range(num_letters):
        list.append(random.choice(string.ascii_letters))
    for i in range(num_zh):
        list.append(chr(random.randint(0x4e00,0x9fbf)))
    for i in range(num_pun):
        list.append(random.choice(string.punctuation))
    random.shuffle(list)
    return ''.join(list)
# print(string.punctuation)
a = create_str(1,1,1,1)
print(a)

