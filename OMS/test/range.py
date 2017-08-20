import random


check_code = ""



for i in range(4):
    current = random.randrange(0,4)
    print(current)
    if current == i:
        tmp = chr(random.randint(65,90))
    else:
        tmp = random.randint(0,9)

    check_code += str(tmp)
print(check_code)




code_list = []
for i in range(10):
    code_list.append(str(i))
for i in range(97, 123):
    code_list.append(chr(i))
baker = random.sample(code_list, 8)
print(code_list)
base_code = "".join((baker))
print(base_code)


current2 = random.randrange(0,4)
print(current2)