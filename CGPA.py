credit = ' '
q =0
g=10
h=9
i=8
j=7
k=6
l=5
m='fail'
def jac(o):


    if sub == 's' :
        return g*3
    elif sub == 'a' :
        return h*3
    elif sub == 'b':
        return i*3
    elif sub == 'c':
        return j*3
    elif sub == 'd':
        return k*3
    elif sub == 'e':
        return l*3
    elif sub == 'f':
        return m
    else:
        print('no answer')
def lab(p):

    if lab1 == 's' :
        return g*2
    elif lab1 == 'a' :
        return h*2
    elif lab1 == 'b':
        return i*2
    elif lab1 == 'c':
        return j*2
    elif lab1 == 'd':
        return k*2
    elif lab1 == 'e':
        return l*2
    elif lab1 == 'f':
        return m
    else:
        print('no answer')
def maths(p):

    if maths1 == 's' :
        return g*4
    elif maths1 == 'a' :
        return h*4
    elif maths1 == 'b':
        return i*4
    elif maths1 == 'c':
        return j*4
    elif maths1 == 'd':
        return k*4
    elif maths1 == 'e':
        return l*4
    elif maths1 == 'f':
        return m
    else:
        print('no answer')
def sem(p):

    if sem1 == 's' :
        return g*1
    elif sem1 == 'a' :
        return h*1
    elif sem1 == 'b':
        return i*1
    elif sem1 == 'c':
        return j*1
    elif sem1 == 'd':
        return k*1
    elif sem1 == 'e':
        return l*1
    elif sem1 == 'f':
        return m
    else:
        print('no answer')
ask1 = int(input('Enter how subjects and labs do you have :'))
ask = int(input('How many subjects do you have in subjects except "Maths" : '))
for sub in range(0,ask):
    sub = (input('Enter how much you have scored :' ))
    print('--------------------------------------')
    print('You scored in this subject is :',jac(sub))
    print('--------------------------------------')
maths1 = (input('How much you scored in math : '))
print('----------------------------------------')
print('You scored in this subject is : ',maths(maths1))
print('---------------------------------------')
print('\n')
the = int(input('How many labs do you have except seminar : '))
for lab1 in range(0,the):
    lab1 = input('Enter how much you have scored :' )
    print('---------------------------------------')
    print('You scored in this subject is : ',lab(lab1))
    print('---------------------------------------')
sem1 = (input('How much you scored in Technical seminar : '))
print('----------------------------------------')
print('You scored in this subject is : ',sem(sem1))
print('---------------------------------------')
print('\n')
print('ADD ALL THE SCORES ')
for s in range(0,ask1):
    s = int(input('Enter a number : '))
    q += s
    credit = q/26
print('-----------------------')
print('Your GPA is : {credit:1.2f}'.format(credit=credit))
print('-----------------------')
