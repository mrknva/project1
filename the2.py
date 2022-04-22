number=str(input())
if number[0]=='?':
    if number[5]=='X':
        d0 = (6 * (10 - 3 * int(number[1]) - 5 * int(number[2]) - 7 * int(number[3]))) % 11
        print(str(d0) + number[1] + number[2] + number[3] + number[4] + digit[5])
    else:
        d0 = (6 * (int(number[5]) - 3 * int(number[1]) - 5 * int(number[2]) - 7 * int(number[3]))) % 11
        print(str(d0) + number[1] + number[2] + number[3] + number[4] + number[5])
if number[1]=='?':
    if number[5]=='X':
        d1 = (4 * (10 - 2 * int(number[0]) - 5 * int(number[2]) - 7 * int(number[3]))) % 11
        print(number[0] + str(d1) + number[2] + number[3] + number[4] + number[5])
    else:
        d1 = (4 * (int(number[5]) - 2 * int(number[0]) - 5 * int(number[2]) - 7 * int(number[3]))) % 11
        print(number[0] + str(d1) + number[2] + number[3] + number[4] + number[5])
if number[2] == "?":
    if number[5] == 'X':
        d2 = (9 * (10 - 2 * int(number[0]) - 3 * int(number[1]) - 7 * int(number[3]))) % 11
        print(number[0] + number[1] + str(d2) + number[3] + number[4] + number[5])
    else:
        d2 = (9 * (int(number[5]) - 2 * int(number[0]) - 3 * int(number[1]) - 7 * int(number[3]))) % 11
        print(number[0] + number[1] + str(d2) + number[3] + number[4] + number[5])
if number[3] == "?":
    if number[5] == 'X':
        d3= (8 * (10 - 2 * int(number[0]) - 3 * int(number[1]) - 5 * int(number[2]))) % 11
        print(number[0] + number[1] + number[2] + str(d3) + number[4] + number[5])
    else:
        d3 = (8 * (int(number[5]) - 2 * int(number[0]) - 3 * int(number[1]) - 5 * int(number[2]))) % 11
        print(number[0] + number[1] + number[2] + str(d3) + number[4] + number[5])
if number[5] == '?':
    d5 = (2 * int(number[0]) + 3 * int(number[1]) + 5 * int(number[2]) + 7 * int(number[3])) % 11
    if d5 == 10:
        print(number[0] + number[1] + number[2] + number[3] + number[4] + 'X')
    else:
        print(number[0] + number[1] + number[2] + number[3] + number[4] + str(d5))
if number.find('?') == -1:
    check = (2 * int(number[0]) + 3 * int(number[1]) + 5 * int(number[2]) + 7 * int(number[3])) % 11
    if number[5]!='X' and check == int(number[5]):
        print("Valid")
    elif number[5]=='X' and check == 10:
        print("Valid")
    else:
        print("Invalid")
        
    
            
