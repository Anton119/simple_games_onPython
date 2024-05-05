import random 
import time 

MIN_OPERAND = 3
MAX_OPERAND = 12
operators = ["+", "-", "*"]
TOTAL_PROBLEMS = 10

def generate_problems():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(operators)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

input("Press Enter to start!")
print("--------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problems()
    while True: 
        guess = input("Problem #" + str(i+1) + ": " + expr + " = ")
        
        if guess == str(answer):
            break

end_time = time.time()
total_time = end_time - start_time

print("--------------------")
print("You've finished in " + str(round(total_time, 2)) + " seconds")

