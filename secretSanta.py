import random

def secretSanta(players):
    result = {}

    names_in_hat = []
    for name in players:
        names_in_hat.append(name)

    for i in players:
        name_in_hat = random.choice(names_in_hat)

        # Avoiding the current player choosing a name from choosing their own.
        while name_in_hat == i:
            name_in_hat = random.choice(names_in_hat)

        result[i] = str(name_in_hat)
        names_in_hat.remove(name_in_hat)

    return result
