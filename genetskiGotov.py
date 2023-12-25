import random

import numpy as np

OPTIMAL = 10000000  # ciljna vrednost
DNA_SIZE = 64  # broj bitova u hromozomu
POP_SIZE = 1000
GENERATIONS = 10000


def f(x):
    # return x**2
    return 0.5 - ((np.sin(x) ** 2 - 0.5) / (1 + 0.001 * x ** 2) ** 2)


def selection(items):  # npr. slucajna selekcija prema kumul. dobrot.
    n = random.uniform(items[0][1], items[len(items) - 1][1])
    for numberI, fitI in items:
        if fitI >= n:
            return numberI, fitI


def random_population():  # kreiraj listu parova (string,dobrota)
    return [(random.uniform(-100, 101), 0) for _ in range(POP_SIZE)]


def fitness(dna):  # funcija dobrote (prilagodljivosti) udaljenost od cilja
    return OPTIMAL - f(dna[0])


def mutate(dna):  # izbegavanje zarobljavanja u lokalnom "dobrom" resenju
    mutation_chance = 0.01
    mutated_num = int(dna[0])
    for x in range(32):
        if random.random() <= mutation_chance:
            mutated_num ^= (1 << x)
    return float(mutated_num), dna[1]


def crossover(dna1, dna2):
    return (dna2[:32] + dna1[32:]), (dna1[:32] + dna2[32:])


def pofitnessu(par):
    return par[1]


# generisanje inicijalne populacije: lista parova (slucajnistring, dobrota)
population = random_population()
new_population = []  # sledeca generacija
# simulacija svih generacija
for generation in range(GENERATIONS):
    # pridruzivanje dobrote hromozomu
    for i in range(len(population)):
        numI = population[i]
        fitnessI = fitness(numI)
        if fitnessI == 0:  # idealan hromozom
            print("GEN:%05f Hromozom: %s Fitness: %05f" % (generation, numI, fitnessI))
            exit(0)
        else:
            population[i] = (population[i][0], fitnessI)
    # sortiranje populacije po dobroti
    population.sort(key=pofitnessu, reverse=False)

    # ispisi najbolji hromozom
    print('GEN:{:05f} Hromozom: {} Fitness:{:05f}'.format(generation, population[0][0], population[0][1]))

    # postavljanje kumulativne dobrote
    cumul = 0
    for i in range(len(population)):
        cumul += population[i][1]
        population[i] = (population[i][0], cumul)
    total = population[len(population) - 1][1]

    for _ in range(POP_SIZE // 2):
        # selekcija roditelja

        par1 = selection(population)
        par2 = selection(population)

        # ukrstanje roditelja i stvaranje dva potpomka
        child1, child2 = crossover(par1, par2)

        # mutacija i punjenje sledece generacije
        new_population.append(mutate(child1))
        new_population.append(mutate(child2))

    new_population.sort(key=pofitnessu, reverse=False)
    population = new_population
    new_population = []
