height = 1.75
weight =80.5
BMI = weight / height**2
if BMI < 18.5:
     print('Too light')
elif BMI > 18.5 and BMI <25:
     print('Normal')
elif BMI > 25 and BMI <28:
     print('Overweight')
elif BMI >28 and BMI < 32:
     print('Too Fat')
elif BMi > 32:
     print('Severe Obesity')
else:
     print('Wrong!')
