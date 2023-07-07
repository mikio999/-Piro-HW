import random

def brGame():
    num = 0
    play_turn = "player"

    while num < 31:
        while True:
            if play_turn == "computer":
                    count = random.randint(1,3)
                    num = num + count
                    break
            else:
                try:
                  count = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
                  if count == 1 or count == 2 or count == 3:
                      num = num + count
                      break
                  else:
                    print("1, 2, 3 중 하나를 입력하세요.")
                except ValueError:
                    print("정수를 입력하세요.")

        for i in range(num - count + 1, num + 1):
            print(f"{play_turn} : {i}")

        if num >= 31:
            winner = "player" if play_turn == "computer" else "computer"
            print(f"{winner} win!")
            break

        if play_turn == "player":
            play_turn = "computer"
        else:
            play_turn = "player"

brGame()
