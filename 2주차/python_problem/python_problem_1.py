num = 0

while True:
  try:
    count = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
    if count == 1 or count == 2 or count == 3:
      break
    else:
     print("1, 2, 3 중 하나를 입력하세요.")
  except ValueError:
    print("정수를 입력하세요.")