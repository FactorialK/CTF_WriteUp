import base64

flag_head = 'picoCTF{'
# for char in flag_head:
#         print(f"{char}:{ord(char)}")
        # print(flag_head[1])
flag = []
with open('./encrpyted.txt','r') as text:
    text_str = text.read()
    for char in text_str:
        if char  in {'{', '_', '}'}:
            flag += [ord(char)]
        elif ord(char) >= 48 and ord(char) <=57:
            if ord(char) - 8 < 48:
                flag += [ord(char)]
                # flag += [57 - 8 + (ord(char) - 48 + 1)]
            else:
                flag += [ord(char)]

        elif ord(char) >= 65 and ord(char) <=90:
            if ord(char) - 8 < 65:
                flag += [90 - 8 + (ord(char) - 65 + 1)]
            else:
                flag += [ord(char) - 8]

        elif ord(char) >= 97 and ord(char) <=122:
            if ord(char) - 8 < 97:
                flag += [122 - 8 + (ord(char) - 97 + 1)]
            else:
                flag += [ord(char)-8]
        # print(f"{char}:{ord(char)-8}", end="")
    print(flag)


    print(text_str)
    for i in range(len(flag)):
        print(chr(flag[i]), end="")