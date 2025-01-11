import random
from collections import defaultdict

def simulate_game():
    urne_blanche = ['noire', 'noire']
    urne_noire = ['blanche', 'blanche']
    urne2_blanche = ['noire', 'noire']
    urne2_noire = ['blanche', 'blanche']
    tour = 0
    joueur2 = 0
    joueur1 = 0

    while True:
        boule_blanche = random.choice(urne_blanche)
        boule_noire = random.choice(urne_noire)

        urne_blanche.remove(boule_blanche)
        urne_noire.remove(boule_noire)

        urne_blanche.append(boule_noire)
        urne_noire.append(boule_blanche)

        tour += 1
        if urne_noire.count('noire') == 2:
            joueur1 += 1
            break

        boule_blanche = random.choice(urne2_blanche)
        urne2_blanche.remove(boule_blanche)

        urne2_noire.append(boule_blanche)
        boule_noire = random.choice(urne2_noire)   
        urne2_noire.remove(boule_noire)
        urne2_blanche.append(boule_noire)

        if urne2_noire.count('noire') == 2:
            joueur2 += 1
            break
    return joueur1,joueur2,tour

def simulate_games(n):
    results = []
    tot1 =0
    tot2 = 0
    tot1 = defaultdict(int)
    tot2 = defaultdict(int)
    for _ in range(n):
        jou1,jou2,tour = simulate_game()
        tot1[tour] += jou1
        tot2[tour] += jou2
        #results.append(simulate_game())
    return tot1,tot2

if __name__ == "__main__":
    n = 10000000
    tot1,tot2 = simulate_games(n)
    # print(f"Résultats des {n} parties : {results}")
    # print(f"Nombre moyen de tours : {sum(results) / n}")
    T1 = T2 = 0
    for i in range(max(len(tot1),len(tot2))+3):
        print(n,tot1.get(i,0)/n*100,tot2.get(i,0)/n*100)
        T1 += tot1.get(i,0)
        T2 += tot2.get(i,0)
    print(n,T1/n*100,T2/n*100, (T1+T2)/n*100)