
fin = open('students.csv','r',encoding='utf-8')
title = fin.readline()
print(title)
students = [x.strip().split(',') for x in fin]
fin.close()
bal_sum = {} 
bal_cnt = {} 
for x in students:

    if x[4]!='None':
        if x[3] in bal_sum:
            bal_sum[x[3]] += int(x[4])
            bal_cnt[x[3]] += 1
        else:
            bal_sum[x[3]] = int(x[4])
            bal_cnt[x[3]] = 1         
    fio = x[1].split()
    if fio[0]=='Хадаров' and fio[1]=='Владимир':
        print(f'Ты получил: {x[4]}, за проект - {x[2]}')
for x in students:
    if x[4]=='None':
        x[4]=f'{bal_sum[x[3]]/bal_cnt[x[3]]:.3f}'
fout = open('student_new.csv','w',encoding='utf-8')
fout.write(title)
for x in students:
    s = ','.join(x)+'\n'
    print(s)
    fout.write(s)
fout.close()
fin = open('students.csv','r',encoding='utf-8')
title = fin.readline()
print(title)
students = [x.strip().split(',') for x in fin]
fin.close()
for i in range(1,len(students)):
    for j in range(i,0,-1):
        if students[j][4]<students[j-1][4]:
            students[j],students[j-1] = students[j-1],students[j]
        else:
            break
cnt = 0
for x in students:
    if '10' in x[3] and x[4]=='5':
        cnt+=1
        fio = x[1].split()
        print(f'{cnt} место: {fio[1][0]}. {fio[0]}')
        if cnt==3:
            break
fin = open('students.csv','r',encoding='utf-8')
title = fin.readline()
print(title)
students = [x.strip().split(',') for x in fin]
fin.close()
while True:
    N = input('Введите № проекта (или СТОП):')
    if N.upper()=='СТОП':
        break
    for x in students:
        if x[2]==N:
            fio = x[1].split()
            print(f'Проект № {x[2]} делал: {fio[1][0]}. {fio[0]} он(а) получил(а) оценку - {x[4]}.')
            break
    else:
        print('Ничего не найдено')
a=False
from random import choice
fin = open('students.csv','r',encoding='utf-8')
title = fin.readline().strip()
print(title)
students = [x.strip() for x in fin]
fin.close()
symbol='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
cifri='0123456789'
big='QWERTYUIOPASDFGHJKLZXCVBNM'
small='qwertyuiopasdfghjklzxcvbnm'
for i in range(len(students)):
    da=0
    ci=0
    bi=0
    sm=0
    s = students[i].split(',')
    fio = s[1].split()
    login = fio[0]+'_'+fio[1][0]+fio[2][0]
    password = ''
    while da!=True:
        for _ in range(8):
            password+=choice(symbol)
            if password[-1] in cifri: ci=1
            if password[-1] in big: bi=1
            if password[-1] in small: sm=1
            if ci+bi+mi==3: da=1
    students[i] = students[i]+','+login+','+password
fout = open('students_password.csv','w',encoding='utf-8')
fout.write(title+',login,password\n')
for x in students:
    s =x+'\n'
    fout.write(s)
fout.close()
