grade={}
homepage=input('欢迎登陆学生BMI指数信息管理系统！按任意键继续\n')
while True:
    print('~~\n欢迎你来到主菜单\n~~')
    menu=('1.录入','2.查询','3.修改','4.删除','5.预览','6.退出')
    for feature in menu:
        print(feature)
    number=('1','2','3','4','5','6')
    order=input('请输入你想要操作的序号：\n')
    if order in number:
        num=int(order)
        while num==1:
            name=input('请输入学生姓名：')
            height=float(input('请输入学生身高（M）:'))
            weight=float(input('请输入学生体重（Kg）：'))
            BMI=weight/height
            grade[name]=BMI
            exit=input('录入成功！按任意键继续录入,按Y返回主菜单\n')
            if exit==('Y'):
                break
            else:
                continue
        while num==2:
            name=input('请输入你要查询的学生姓名：')
            if name in grade:
                if grade[name]<=18.5:
                    print('%s的BMI指数为%.1f，偏瘦。要多吃肉！' %(name,grade[name]))
                elif 18.5<grade[name]<=24:
                    print('%s的BMI指数为%.1f，标准。迷人身材！' %(name,grade[name]))
                elif 24<grade[name]<=27:
                    print('%s的BMI指数为%.1f, 过重。肉肉哒，要管住嘴！' %(name,grade[name]))
                elif 28<grade[name]<=32:
                    print('%s的BMI指数为%.1f，肥胖。迈开腿去运动吧！' %(name,grade[name]))
                else:
                    print('%s的BMI指数为%.0f，超重。最讨厌的死肥宅!' %(name,grade[name]))
                exit=input('查询成功！\n按Y继续查询,按任意键返回主菜单\n')
                if exit=='Y':
                    continue
                else:
                    break
            else:
                exit=input('查无此人！\n按任意键继续查询,按N返回主菜单\n')
                if exit!='N':
                    continue
                else:
                    break
        while num==3:
            name=input('请输入你要修改的学生的姓名:')
            if name in grade:
                height=float(input('请输入学生身高（M）:'))
                weight=float(input('请输入学生体重（Kg）：'))
                BMI=weight/height
                grade[name]=(BMI)
                exit=input('修改成功！按Y继续修改，按任意键返回主菜单\n')
                if exit=='Y':
                    continue
                else:
                    break
            else:
                print('查无此人，请重新输入！')
                continue
        while num==4:
            name=input('请删除你要删除的学生的姓名：')
            if name in grade:
                grade.pop(name)
                exit=input('删除成功！按Y继续删除，按任意键返回主菜单\n')
                if exit=='Y':
                    continue
                else:
                    break
            else:
                print('查无此人，请重新输入！')
                exit2=input('按Y继续删除，按任意键返回主菜单\n')
                if exit2=='Y':
                    continue
                else:
                    break
        while num==5:
            print(grade)
            exit=input('预览成功！按任意键返回主菜单\n')
            break
        if num==6:
            print('感谢你的使用，再见！\n')
            break
        elif order not in number:
            print('输入有误，请输入序号1~6')
            continue