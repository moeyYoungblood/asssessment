# random question/number generator
import random
random_num = random.randint(1, 4)

random_num1 = random.randint(1, 10)
random_num2 = random.randint(1, 10)
random_sum = random_num1 + random_num2
if random_num == 1:
     print(f"{random_num1} + {random_num2} = {random_num1 + random_num2}")
if random_num == 2:
     print(f"{random_num1} - {random_num2} = {random_num1 - random_num2}")
if random_num == 3:
    print(f"{random_num1} / {random_num2} = {random_num1 / random_num2}")
if random_num == 4:
    print(f"{random_num1} * {random_num2} = {random_num1 * random_num2}")

