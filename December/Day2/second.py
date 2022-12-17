def calculatePick(enemyPick, outcome):
    results = {
        ("A", 6): 2,
        ("B", 6): 3,
        ("C", 6): 1,

        ("A", 3): 1,
        ("B", 3): 2,
        ("C", 3): 3,
        
        ("A", 0): 3,
        ("B", 0): 1,
        ("C", 0): 2
    }
    return results.get((enemyPick, outcome), 0)
    

def playGame(data):
    score = 0
    mapping = {
        "X": 0,
        "Y": 3, 
        "Z": 6 
    }
    for i in data:
        enemyPick, outcome = i.split(" ")
        score += mapping[outcome] + calculatePick(enemyPick, mapping[outcome])
    return score

with open("puzzle.txt") as file:
    data = file.read().splitlines()
    print(playGame(data))
    file.close()