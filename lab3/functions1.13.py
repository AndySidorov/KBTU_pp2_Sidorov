import random
def GTN(num):
    global cnt
    print("Take a guess.")
    g = int(input())
    if g < num:
        print("Your guess is too low.")
        cnt += 1
        GTN(num)
    elif g > num:
        print("Your guess is too high.")
        cnt += 1
        GTN(num)
x = random.randrange(1,21)
cnt = 1
print("Hello! What is your name?")
name = input()
txt1 = "Well, {}, I am thinking of a number between 1 and 20."
print(txt1.format(name))
GTN(x)
txt2 = "Good job, {}! You guessed my number in {} guesses!"
print(txt2.format(name,cnt))