def creat_field():
    field = []
    for i in range(3):
        field.append(['*'] * 3)

    return field

def print_field(field):
    for i in range(3):
        for j in range(3):
            print(field[i][j], end='')
        print()


def win(field):
    for i in range(3):
        if field[i][1] != '*' and field[i][0] == field[i][1] == field[i][2]:
            return True
        
    for i in range(3):
        if field[0][i] != '*' and field[0][i] == field[1][i] == field[2][i]:
            return True        

    if field[0][0] != '*' and field[0][0] == field[1][1] == field[2][2]:
        return True

    if field[0][2] != '*' and field[0][2] == field[1][1] == field[2][0]:
        return True    

    return False
    
    


def end_game(field):
    if win(field):
        return True

    for i in range(3):
        for j in range(3):
            if field[i][j] == '*':
                return False
            

def right_number(a):
    if a > 0 and a < 4:
        return True
    else:

        return False




while True:
    field=creat_field()
    
    current_symbol = 'X'
    
    while not end_game(field):
        print_field(field)
        print('Введите номер строки и номер столбца')
        print('Введите номер строки')
        row = int(input())
        if right_number(row) == False:
            print('Введите правильное число от 1 до 3.')
            continue

        else:
            print('Теперь введите номер столбца')
            column = int(input())
            if right_number(column) == False:
                print('Введите правильное число от 1 до 3.')
                continue

   


        if field[row - 1][column - 1] == '*':
            field[row - 1][column - 1] = current_symbol
        else:
            print('Это поле уже занято')
            continue
    
        if current_symbol == 'X':
            current_symbol = '0'
        else:
            current_symbol = 'X'
    
    print_field(field)
    if current_symbol == 'X':
        print('Ура победил 0!')
    else:
        print('Ура победил Х!')