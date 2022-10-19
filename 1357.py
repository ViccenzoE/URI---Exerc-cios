braille = [".*\n**\n.. ", "*.\n..\n.. ", "**\n*.\n.. ", "**\n..\n.. ", "*.\n.*\n.. ", "**\n.*\n.. ", "**\n**\n.. ", "*.\n*.\n.. ", ".*\n.*\n.. ", ".*\n.*\n.. "]

d = int(input())
sb = input()
if sb == "S":
    num = str(input())
    for i in range(len(num)):
        for x in braille:
            if i == x:
                print(braille[x])