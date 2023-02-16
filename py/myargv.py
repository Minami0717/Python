import random

lotto=[]
for i in range(6):
    num = random.randint(1,45)
    if num not in lotto:
        lotto.append(num)

print(lotto)
