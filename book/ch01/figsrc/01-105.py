import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
# colonnes : x de départ et largeur
C = [(26, 10), (38, 10), (50, 10), (62, 14)]
def row(y, labels, roles, lws=None):
    for (x, w), lab, r, lw in zip(C, labels, roles, lws or [0.8]*4):
        if lab is not None:
            box(ax, x, y, w, 8, r, label=lab, lw=lw)
row(60, ['3', '9', '7', '000'], ['fixe', 'sujet', 'varie', 'fixe'], [0.8, 1.4, 0.8, 0.8])
text(ax, 43, 77, "chiffre d'arrondi : 9", 'sujet', 's')
line(ax, [(43, 75.8), (43, 68)], 'sujet', lw=0.8)
text(ax, 55, 72, 'témoin : 7', 'varie', 's')
arrow(ax, (43, 60), (43, 43), 'varie')
box(ax, 26, 34, 10, 8, 'fixe', label='3')
box(ax, 38, 34, 10, 8, 'limite', label='10')
text(ax, 66, 38, '9 + 1 = 10 : déborde', 'limite', 's')
arrow(ax, (43, 34), (43, 17), 'varie')
arrow(ax, (40, 34), (31, 17), 'varie')
text(ax, 66, 25, '0 ici, 1 à gauche', 'varie', 's')
row(8, ['4', '0', '0', '000'], ['resultat']*4)
save(fig, '01-105')
