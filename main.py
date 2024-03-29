from src.helpers import *

if __name__ == "__main__":
    mode = input("Choose your mode:\n1. Host game\n2. Auto accept game")
    if mode ==  '1':
        while True: 
            create_match()
            time.sleep(300)
            auto_move()
            time.sleep(300)
            auto_move()
            time.sleep(50)

    if mode == '2':
        auto_accept_match() 