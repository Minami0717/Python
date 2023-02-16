import random

while True:
    print("주사위 굴리기: 1 종료: 2")
    choice = int(input())
    
    if choice == 1:
        p1 = random.randrange(1,7)
        p2 = random.randrange(1,7)
        c1 = random.randrange(1,7)
        c2 = random.randrange(1,7)

        print("플레이어의 주사위 숫자는 %d %d입니다." % (p1,p2))
        print("컴퓨터의 주사위 숫자는 %d %d입니다." % (c1,c2))

        if p1+p2>c1+c2:
            print("플레이어가 이겼네요.")
        elif p1+p2<c1+c2:
            print("컴퓨터가 이겼네요.")
        else:
            print("둘이 비겼네요.")
        print("")
        
    elif choice == 2:
        break
