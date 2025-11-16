import random

cons = "bcdfghjklmnpqrstvwxyz"
vows = "aeiou"

def generate_random_word():
    word = ""
    
    pattern = random.choice(["CVC", "CC", "VV", "VCV", "VC", "CV"])
    
    for _ in range(random.randint(2, 3)):
        for x in pattern:
            word += random.choice(random.choice(cons) if x == "C" else random.choice(vows))
            
    return word
    
for _ in range(100):
    print(generate_random_word())
