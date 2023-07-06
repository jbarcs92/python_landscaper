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

current_tool = 'teeth'


while cash_total < 5:
    phrase = input('Did you cut grass today?: ').lower()
    if phrase == 'yes' and cash_total < 5:
        cash_total += 1
        print(f'Your cash total is ${cash_total}')
    if phrase == 'no' and cash_total < 5:
        print(f'Your cash total is ${cash_total}')

if current_tool == 'teeth' and cash_total >= 5:
     phrase = input('Would you like to upgrade to some rusty scissors for $5?: ')
     if phrase == 'yes':
         cash_total -= 5
         current_tool = 'rusty scissors'
         print(f'Your cash total is ${cash_total}')  

while current_tool == 'rusty scissors' and cash_total < 25:
    phrase = input('Did you cut grass today?: ').lower()
    if phrase == 'yes' and cash_total < 25:
        cash_total += 5
        print(f'Your cash total is ${cash_total}')
    if phrase == 'no' and cash_total < 25:
        print(f'Your cash total is ${cash_total}')

if current_tool == 'rusty scissors' and cash_total >= 25:
     phrase = input('Would you like to upgrade to an old lawnmower for $25?: ')
     if phrase == 'yes':
         cash_total -= 25
         current_tool = 'old lawnmower'
         print(f'Your cash total is ${cash_total}') 

while current_tool == 'old lawnmower' and cash_total < 250:
    phrase = input('Did you cut grass today?: ').lower()
    if phrase == 'yes' and cash_total < 250:
        cash_total += 50
        print(f'Your cash total is ${cash_total}')
    if phrase == 'no' and cash_total < 250:
        print(f'Your cash total is ${cash_total}')

if current_tool == 'old lawnmower' and cash_total >= 250:
     phrase = input('Would you like to upgrade to battery-powered lawnmower for $250?: ')
     if phrase == 'yes':
         cash_total -= 250
         current_tool = 'battery-powered lawnmower'
         print(f'Your cash total is ${cash_total}') 

while current_tool == 'battery-powered lawnmower' and cash_total < 500:
    phrase = input('Did you cut grass today?: ').lower()
    if phrase == 'yes' and cash_total < 500:
        cash_total += 100
        print(f'Your cash total is ${cash_total}')
    if phrase == 'no' and cash_total < 500:
        print(f'Your cash total is ${cash_total}')
    
    



