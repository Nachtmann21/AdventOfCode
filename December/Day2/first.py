def calculateWinner(enemyPick, myPick):
    results = {
        ("A", "B"): 0,
        ("A", "C"): 6,
        ("B", "A"): 6,
        ("B", "C"): 0,
        ("C", "A"): 0,
        ("C", "B"): 6
    }
    return results.get((myPick, enemyPick), 3) # 3 if myPick == enemyPick
    

def playGame(data):
    score = 0
    mapping = {
        "X": ("A", 1),
        "Y": ("B", 2),
        "Z": ("C", 3)
    }
    
    for i in data:
        enemyPick, myPick = i.split(" ")
        score += mapping[myPick][1] + calculateWinner(enemyPick, mapping[myPick][0])
    return score

with open("puzzle.txt") as file:
    data = file.read().splitlines()
    print(playGame(data))
    file.close()

