import os,shutil
import sys
import time
import easygui as g

name = []
while True:
    temp = str(g.enterbox(msg="input the file keyword(type -1 to stop keyword typing): "))
    if temp == "-1":
        break
    else:
        name.append(temp)
# print(name)

from_list = ["D:","E:","F:","G:"]
avaliable_from = g.choicebox(msg='choice the driver', title='^_^', choices=from_list)
# print(avaliable_from)

default = r'C:\Users'
move_path = g.diropenbox(msg='choice the folder you want to save files', title='^_^',default=default)
# print(move_path)


while 1:
    try:
        lst = os.listdir(avaliable_from)
    except FileNotFoundError:
        continue
    else:
        while 1:
            for root, dirs, files in os.walk(avaliable_from, topdown=True):
                for file in files:
                    ex = os.path.splitext(file)[0]
                    # print(ex)
                    # print(root,ex)
                    for word in name:
                        if word in ex:
                            copy_path = root+"\\" + file
                            shutil.copy(copy_path,move_path)
            time.sleep(120)













# for path in lst:
#     for root, dirs, files in os.walk(path, topdown=True):
#         for file in files:
#             ex = os.path.splitext(file)[0]
#             print(ex)
#             # print(root,ex)
#             for word in name:
#                 if word in ex:
#                     copy_path =  root+"\\"+file
#                     shutil.copyfile(copy_path,move_path)
#                     print("copy complete")
