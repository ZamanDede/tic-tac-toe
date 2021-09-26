
finished = True

def print_table():
    table = "_ _ _
    _ _ _
    _ _ _"
def update_table(pos,mark):
    pass
def check_result():
    pass


def play_game():
    while finished:
        print_table()
        player1p = input("player 1 choose a position 1-9: ")
        player1m = input("player 1 choose a mark x-o: ")
        update_table(player1p,player1m)
        print_table()
        check_result()
        player2p = input("player 2 choose a position 1-9: ")
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