

score=102

if score>=101:
  print('Not valid')
  exit()
if score>=90:
   grade='A'
elif score>=80:
   grade='B'
elif score>=70:
   grade='C'
elif score>=60:
   grade='D'
elif score>=50:
   grade='E' 
else:
   grade='F'   
print('Your grade is ',grade)