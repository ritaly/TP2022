def cal_bmi(weight, height):
    bmi = weight / height ** 2
    return round(bmi, 2)

#--------
print('***** WITAJ W BMI KALKULATORZE ******')
w = float(input('Give me your weight? [kg] --->'))
h = float(input('Give me your height? [m] --->'))

result = cal_bmi(w, h)

print('Your BMI is:', result)