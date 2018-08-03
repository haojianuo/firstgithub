with open('D:/workspase/frstPython/firstgithub/code/test.txt', 'w') as file_object:
    n=1
    file_object.write("I love programming.")
    file_object.write(str(n))
    file_object.writelines(str(n))