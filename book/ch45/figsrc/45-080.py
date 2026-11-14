import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
D = ['ne bouge rien', 'avance d’un cran', 'avance de 2 crans', 'avance de 3 crans']
box(ax, 2, 6, 84, 70, 'resultat', fill=False, dash=True)
text(ax, 44, 83, r'$G_L$ : 4 applications', 'resultat', 'm')
for k in range(4):
    y = 56 - k * 16
    box(ax, 8, y, 24, 12, 'sujet', label=rf'${k}_L$', size='l'); text(ax, 38, y + 6, D[k], 'encre', 's', ha='left')
save(fig, '45-080')
