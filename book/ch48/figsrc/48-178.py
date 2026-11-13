import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def row(y, n, step, tit, res):
    xs = [44 - (n - 1) * 2.7 + i * 5.4 for i in range(n)]
    for i, x in enumerate(xs):
        hit = i % step == 0
        disc(ax, x, y, 2.0, 'sujet' if hit else 'fixe')
    brace(ax, xs[0] - 2, xs[-1] + 2, y + 4, 'fixe', None, down=False, depth=1.6)
    text(ax, 44, y + 9.5, tit, 'fixe', 's')
    text(ax, 44, y - 6, res, 'resultat', 'm', weight='bold')
    return xs
row(58, 12, 3, 'horloge à 12 : 12 éléments', '12 ÷ 3 = 4 éléments en bleu')
row(22, 10, 2, 'horloge à 10 : 10 éléments', '10 ÷ 2 = 5 éléments en bleu')
text(ax, 44, 40, 'de 3 en 3, puis de 2 en 2', 'varie', 's')
save(fig, '48-178')
