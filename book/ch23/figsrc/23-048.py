import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
k = 1.48
def row(y, title, l, rl, lr, rr, sign, srole):
    text(ax, 44, y + 14, title, 'fixe', 's')
    box(ax, 40 - l * k, y, l * k, 9, lr, label=str(l))
    box(ax, 48, y, rl * k, 9, rr, label=str(rl))
    text(ax, 44, y + 4.5, sign, srole, 'l')
row(52, 'au départ', 16, 16, 'fixe', 'fixe', '=', 'fixe')
row(28, '9 ajouté d’un seul côté', 25, 16, 'varie', 'fixe', '≠', 'limite')
row(4, '9 ajouté des deux côtés', 25, 25, 'resultat', 'resultat', '=', 'resultat')
save(fig, '23-048')
