import random

def game_score():
    print("Welcome to the game!")
    score = random.randint(0, 100)
    # fetch the high score
    with open("highscore.txt") as f:
        high_score = f.read()
        if high_score != "":
            high_score = int(high_score)
        else:
            high_score = 0

    print(f"Your score: {score}")
    # write this high_score to the file
    if score > high_score:
        with open("highscore.txt", "w") as f:
            f.write(str(score))

    return score

game_score()