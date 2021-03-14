import os
import re

file = os.getcwd() + os.sep + "sh10.comp"

fufile = open(file)

brx = 0
brxi = 0
brxo = 0
tool = []
toolk = []
toolv = []
btool = False
btoolk = False
btoolv = False

for l in fufile:
    br_in = re.findall(r"\{", l)
    br_out = re.findall(r"\}", l)
    br_in_num = int(len(br_in))
    br_out_num = int(len(br_out))

    # print(l.strip())

    if br_in_num > 0 or br_out_num > 0:
        if br_in_num != 0:
            brxi += br_in_num
        if br_out_num != 0:
            brxo += br_out_num
        brx = brxi - brxo
        # print(f"{brxi} - {brxo}")
        # print(brx)

    if brx == 0:
        tool.append(l.strip())
        # print(l.strip())
        # print("000000000000000000000000000000000000")

    if brx == 1 and btool is False:
        # print(l.strip())
        # print("111111111111111111111111111111111111")
        tool.append(l.strip())
        btool = True
    else:
        btool = False

    if brx == 2 and btoolk is False:
        # print(l.strip())
        # print("222222222222222222222222222222222222")
        toolk.append(l.strip())
        btoolk = True
    else:
        btoolk = False

    if brx == 3 and btoolv is False:
        toolk.append(l.strip())
        # print(l.strip())
        # print("3333333333333333333333333333333333333")
        btoolv = True
    else:
        btoolv = False

    if brx > 3:
        # print(l.strip())
        toolv.append(l.strip())
# print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")
# print(tool)
# print(toolk)
# print(toolv)

for v in toolv:
    print(v)








