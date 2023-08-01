s1=float(input('English:'))
s2=float(input('Tamil:'))
s3=float(input('Maths:'))
s4=float(input('Science:'))
s5=float(input('Social Science:'))
p=50
total=s1+s2+s3+s4+s5+p
if total>=495:
    print('S grade')
elif total>=490:
    print('A grade')
elif total>=480:
    print('B grade')
elif total>=450:
    print('C grade')
elif total>=400:
    print('D grade')
elif total>=350:
    print('A grade')
else:
    print('U grade')