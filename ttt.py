



table = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def print_table():
    print("\n")
    print(table[0] + " | " + table[1] + " | " + table[2] + "     1 | 2 | 3")
    print(table[3] + " | " + table[4] + " | " + table[5] + "     4 | 5 | 6")
    print(table[6] + " | " + table[7] + " | " + table[8] + "     7 | 8 | 9")
    print("\n")
    
def update_table(pos,mark,player):
    if table[pos-1] == "-":
        table[pos-1] = mark
    else:
        print("The position is full!")
        if player == 1:
            player1()
        else:
            player2()
    
def check_result(player):
    
    if table[0] == "x" and table[1] == "x" and table[2] == "x":
        print("player{} is the winner".format(player))
        raise SystemExit
    elif table[3] == "x" and table[4] == "x" and table[5] == "x":
        print("player{} is the winner".format(player))
        raise SystemExit
    elif table[6] == "x" and table[7] == "x" and table[8] == "x":
        print("player{} is the winner".format(player))
        raise SystemExit
    elif table[0] == "x" and table[3] == "x" and table[6] == "x":
        print("player{} is the winner".format(player))
        raise SystemExit
    elif table[1] == "x" and table[4] == "x" and table[7] == "x":
        print("player{} is the winner".format(player))
        raise SystemExit
    elif table[2] == "x" and table[5] == "x" and table[8] == "x":
        print("player{} is the winner".format(player))
        raise SystemExit
    elif table[0] == "x" and table[4] == "x" and table[8] == "x":
        print("player{} is the winner".format(player))
        raise SystemExit
    elif table[2] == "x" and table[4] == "x" and table[6] == "x":
        print("player{} is the winner".format(player))
        raise SystemExit
    
    elif table[0] == "o" and table[1] == "o" and table[2] == "o":
        print("player{} is the winner".format(player))
        raise SystemExit
    elif table[3] == "o" and table[4] == "o" and table[5] == "o":
        print("player{} is the winner".format(player))
        raise SystemExit
    elif table[6] == "o" and table[7] == "o" and table[8] == "o":
        print("player{} is the winner".format(player))
        raise SystemExit
    elif table[0] == "o" and table[3] == "o" and table[6] == "o":
        print("player{} is the winner".format(player))
        raise SystemExit
    elif table[1] == "o" and table[4] == "o" and table[7] == "o":
        print("player{} is the winner".format(player))
        raise SystemExit
    elif table[2] == "o" and table[5] == "o" and table[8] == "o":
        print("player{} is the winner".format(player))
        raise SystemExit
    elif table[0] == "o" and table[4] == "o" and table[8] == "o":
        print("player{} is the winner".format(player))
        raise SystemExit
    elif table[2] == "o" and table[4] == "o" and table[6] == "o":
        print("player{} is the winner".format(player))
        raise SystemExit
    else:
        a = 0
        for i in table:
            if i == "-":
                a += 1
        if a == 0:
            print("It's a draw!")
            raise SystemExit
            
    
        

def player1():
    print_table()
    while True:
        player1p = int(input("player 1 choose a position 1-9: "))
        if 0<player1p<10:
            player1m = input("player 1 choose a mark x-o: ")
            if player1m == "x" or player1m == "o":
                break
            else:
                print("Invalid mark try again!")
        else:
            print("Invalid position try again!")
            
    update_table(player1p,player1m,1)
    print_table()
    check_result(1)
        
def player2():
    while True:
        player2p = int(input("player 2 choose a position 1-9: "))
        if 0<player2p<10:
            player2m = input("player 2 choose a mark x-o: ")
            if player2m == "x" or player2m == "o":
                break
            else:
                print("Invalid mark try again!")
        else:
            print("Invalid position try again!")
    update_table(player2p,player2m,2)
    print_table()
    check_result(2)
    
def play_game():
    
    while True:
        player1()
        player2()
            
        
        



play_game()

