import random

# Generate 5 unique random lottery numbers between 1 and 90
lottery_numbers = random.sample(range(1, 91), 5)
print(f"Generated lottery numbers: {lottery_numbers}")

# Read the player data from the file
players = {}
try:
    with open('02_feladat.txt', 'r') as f:
        for line in f:
            name, numbers_str = line.strip().split(';')
            numbers = [int(n) for n in numbers_str.split(',')]
            players[name] = numbers
except FileNotFoundError:
    print("Error: 02_feladat.txt not found.")
    exit()

# Count hits for each player
player_hits = {}
for name, numbers in players.items():
    hits = sum(1 for number in numbers if number in lottery_numbers)
    player_hits[name] = hits

# Write results to a new file
with open('02_eredmeny.txt', 'w') as f:
    for name, hits in player_hits.items():
        f.write(f"{name};{hits}\n")

print("Results written to 02_eredmeny.txt")