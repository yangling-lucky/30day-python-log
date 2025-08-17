"""
用 dict 存姓名→电话
提供 add(name,tel)、find(name)、delete(name) 三个函数
主程序循环读 input()，直到用户输入 q 退出。
"""
phonebook = {}
def add(name,tel):
     if name not in phonebook:
         phonebook[name] = tel
     else:
         print("电话簿中已存在该人员")

def find(name):
    if name in phonebook:
        return phonebook[name]
    else:
        return None

def delete(name):
    if name in phonebook:
        del phonebook[name]
        return True
    else:
        return False

while True:
    message = input("请输入您想进行的操作（add、find、delete、输入q表示结束操作）：")
    if message == "q":
        exit()
    elif message == "add":
        name = input("请输入所添加人员姓名：")
        tel = input("请输入对应人员电话：")
        add(name,tel)
    elif message == "find":
        name = input("请输入所查找人员姓名：")
        print('您所查找人员的电话为：',find(name))
    elif message == "delete":
        name = input("请输入所删除人员姓名：")
        delete(name)
    else:
        print("无效的操作，请重新输入！")

