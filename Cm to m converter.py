'''This Program converts Centi Meters to Meters'''

print('You can enter centimeters and convert them into meters')
while True:
    try:
        cm = float(input('Enter Centi Meters: '))
        m = cm/100
        print(f'{cm} cm is equal to {m:.5} Meters')
    except ValueError:
        print('Please Enter a Value in integer format or Decimal form.')
    
    repeat = input("Do you want to convert one more value? Enter Yes or No: ").strip().lower()
    
    while repeat not in ("yes", "no"):
        print('Please enter Yes or No!')
        repeat = input("Do you want to convert one more value? Enter Yes or No: ").strip().lower()

    if repeat == "no":
        print('Thank you for using our service, see you soon!')
        break
