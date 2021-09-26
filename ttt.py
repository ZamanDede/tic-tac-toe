
finished = True

table = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def print_table():
    print("\n")
    print(table[0] + " | " + table[1] + " | " + table[2] + "     1 | 2 | 3")
    print(table[3] + " | " + table[4] + " | " + table[5] + "     4 | 5 | 6")
    print(table[6] + " | " + table[7] + " | " + table[8] + "     7 | 8 | 9")
    print("\n")
    
def update_table(pos,mark):
    table[pos-1] = mark
def check_result():
    pass


def play_game():
    while finished:
        print_table()
        player1p = int(input("player 1 choose a position 1-9: "))
        player1m = input("player 1 choose a mark x-o: ")
        update_table(player1p,player1m)
        print_table()
        check_result()
        player2p = int(input("player 2 choose a position 1-9: "))
        player2m = input("player 2 choose a mark x-o: ")
        update_table(player2p,player2m)
        print_table()
        check_result()



play_game()

'''
print("_ _ _")
print("_ _ _")
print("_ _ _")

'''