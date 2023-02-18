men_over25 = 0                  # men who earn over R25,000
women_under20 = 0               # women who earn under R20,000

while True:

    emp_no = int(input('employee number? '))
    if emp_no == 0:
        break
    gender = input('gender? ')
    salary = int(input('salary? '))

    if gender == 'male' and salary > 25000:
        men_over25 += 1

    elif gender == 'female' and salary < 20000:
        women_under20 += 1

print(f'The number of men earning above R25000:{men_over25}')
print(f'The number of women earning under R20000:{women_under20}')


