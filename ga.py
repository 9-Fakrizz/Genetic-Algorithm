import numpy as np

def display(p):
    print(p.reshape((3,3)))

def fitness(p):
    p = p.reshape((3,3))
    sum_rows = p.sum(axis = 0)
    sum_cols = p.sum(axis = 1)
    sum_diag = [np.sum(np.diag(p)), np.sum(np.diag(np.fliplr(p)))]
    sum_all = np.concatenate((sum_rows,sum_cols,sum_diag))
    return len(np.unique(sum_all))

n = 100
pop = []
for i in range(n):
    p = np.arange(1,10)
    np.random.shuffle(p)
    pop.append(p)

pop = np.array(pop)
while True:
    fit =[]
    for p in pop:
        fit.append(fitness(p))

    fit = np.array(fit)
    idx = fit.argsort()
    best = fit[idx[0]]
    print(best)
    pop = pop[idx]

    if best == 1:
        display(pop[0])
        break

    for i in range(1, n):
        idx = np.random.choice(9, 2)
        pop[i][idx] = pop[i][idx[::-1]]
