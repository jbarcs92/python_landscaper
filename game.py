teeth = {
    'tool': 'teeth',
    'pay': 1,
    'value': 0
}

scissors = {
    'tool': 'rusty scissors',
    'pay': 5,
    'value': 5
}

old_lawnmower = {
    'tool': 'old lawnmower',
    'pay': 50,
    'value': 25
}

battery_lawnmower = {
    'tool': 'battery lawnmower',
    'pay': 100,
    'value':  250
}

students = {
    'tool': 'students',
    'pay': 250,
    'value': 500
}

cash_total = 0

current_tool = ''


while cash_total < 5:
    phrase = input('Did you cut grass today?: ').lower()
    if phrase == 'yes' and cash_total < 5:
        cash_total += 1
        print(f'Your cash total is ${cash_total}')
    if phrase == 'no' and cash_total < 5:
        print(f'Your cash total is ${cash_total}')

# if cash_total == 5:
#      phrase = input('Would you like to upgrade to some rusty scissors for $5?: ')
#      if phrase == 'yes':
#          cash_total = 0
#          current_tool = 'rusty scissors'
#          print(f'Your cash total is ${cash_total}')
    
    



