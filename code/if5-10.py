current_users = ['haojianuo','tom','alice','peggy','anna']
new_users = ['jay','taylor','ally','haojianuo','tom']
for x in new_users:
    if x in current_users:
        print('请输入其他用户名')
    else:
        print('这个用户名未被使用')
