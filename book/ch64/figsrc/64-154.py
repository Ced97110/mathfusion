import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
bh, bw = 9, 30
ys = [58, 36, 14]

def chain(x, sizes, factors, title):
    text(ax, x + bw / 2, 76, title, 'encre', 's')
    for k, (s, y) in enumerate(zip(sizes, ys)):
        box(ax, x, y, bw, bh, 'resultat', label=s)
    for k, f in enumerate(factors):
        arrow(ax, (x + bw / 2, ys[k] - 0.3), (x + bw / 2, ys[k + 1] + bh + 0.3), 'resultat')
        text(ax, x + bw / 2 + 3, (ys[k] + ys[k + 1] + bh) / 2, f, 'resultat', 's', ha='left')

chain(4, ['6', '3', '1'], ['facteur 2', 'facteur 3'], r'$F$ = les fractions')
# à droite : racines de l'unité ajoutées, le groupe a 3 éléments
text(ax, 73, 76, "avec les racines de 1", 'encre', 's')
box(ax, 58, ys[1], bw - 2, bh, 'resultat', label='3')
box(ax, 58, ys[2], bw - 2, bh, 'resultat', label='1')
arrow(ax, (72, ys[1] - 0.3), (72, ys[2] + bh + 0.3), 'resultat')
text(ax, 75, (ys[1] + ys[2] + bh) / 2, 'facteur 3', 'resultat', 's', ha='left')
text(ax, 44, 4, 'tous les facteurs sont abéliens', 'resultat', 's')
save(fig, '64-154')
