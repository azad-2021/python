students_name = ['Rohan', 'Amita', 'Shushant', 'Pawan', 'Kiran']
students_marks = [67,34,78,85,65]

#zipping names and marks of students

zip_list = zip(students_name,students_marks)
zip_list = list(zip_list)
print('zipped list >> ')
print(zip_list,'\n')

#unzip list

students_name,students_marks = zip(*zip_list)
print('unzipped list >> ')
print('names = ', list(students_name))
print('marks = ', list(students_marks))

list1=[2,4,6,8]

list2=[4,16,36,64,100,121]

ans=zip(list1,list2)

print(list(ans))
print([i.lower() for i in 'python'])