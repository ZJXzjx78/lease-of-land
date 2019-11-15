def print_student_files(name,gender='男',age='20',college='工商学院'):
    print('我叫' + name)
    print('我今年' + str(age) +'岁')
    print('我是' + gender + '生')
    print('我在' + college + '上学')

print_student_files('小明','男', 20,'工商学院') 
print('~~~~~~~~~~~~~~~~~~~~')
print_student_files('小计')
print('~~~~~~~~~~~~~~~~~~~~')
print_student_files('施工队','女',18)