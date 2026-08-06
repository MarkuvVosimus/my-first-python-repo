# bill splitter very gut program but useless but good
bill_amount = input('Please enter amount with cents: ')
tip = input('Please enter tip in percent: ')
people = input('Please enter amount of people: ')
# peak security validation
try:
    bill_amount = float(bill_amount)
    tip = float(tip)
    people = float(people)
except ValueError:
    print("All values must be numbers.")
    quit()
# logik
tip_amount = bill_amount * (int(tip) / 100)
bill_with_tip = bill_amount + tip_amount
bill_per_person = bill_with_tip / people
if str(bill_per_person)[::-1].find('.') > 2:
    float(bill_per_person)
    bill_per_person = round(bill_per_person, 2)
print(f'Each person will pay: ${bill_per_person}')
# tenk you bradar pak you bradar no copyright use anywhere

