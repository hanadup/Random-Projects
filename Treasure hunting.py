print('''
      .--..--..--..--..--..--.
    .' \  (`._   (_)     _   /
  .'    |  '._)         (_)  |
  \ _.')\      .----..---.   /
  |(_.'  |    /    .-\-.  \  |
  \     0|    |   ( O| O) | o|
   |  _  |  .--.____.'._.-.  |
   \ (_) | o         -` .-`  |
    |    \   |`-._ _ _ _ _\ /
    \    |   |  `. |_||_|   |
    | o  |    \_      \     |     -.   .-.
    |.-.  \     `--..-'   O |     `.`-' .'
  _.'  .' |     `-.-'      /-.__   ' .-'
.' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
`-._  `.  |________/\_____|    `-.'
   .'   ).| '=' '='\/ '=' |
   `._.`  '---------------'
           //___\   //___\\
             ||       ||
             ||_.-.   ||_.-.
            (_.--__) (_.--__)
''')
print("Welcome to Treasure Island. Your mission is to find the treasure")
direction = input("Choose a direction? left or right ").lower()

if direction == "left":
    lake = input ("You have choosen left and ended up at a lake,Do you want to swim or wait by the lake? ").lower()
    if lake == "wait":
        door = input("you have arrived at 3 doors, red, blue or yellow door? ").lower()
        if door == "yellow":
            print("you win")
        else:
            print("game over")
    else: 
        print("Game over you have got eaten by a dolphin")
else:
    print("You choose the wrong direction. Game Over")
