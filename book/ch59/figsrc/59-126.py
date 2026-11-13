import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def barre(y, role, nom, zeros, hors):
    f = numberline(ax, 10, 74, y, 0, 20, step=1, every=10, arrow_right=False, role='fixe')
    text(ax, 44, y + 16, nom, role, 's', weight='bold')
    for k in zeros:
        disc(ax, f(k), y + 6, 2.0, 'resultat')
        line(ax, [(f(k), y + 1.5), (f(k), y + 4)], 'resultat', lw=0.7)
    for k in hors:
        disc(ax, f(k), y + 6, 2.0, 'varie')
        line(ax, [(f(k), y + 1.5), (f(k), y + 4)], 'varie', lw=0.7)
    return f
f1 = barre(56, 'sujet', 'ℤ/20 : on ajoute 1', (0, 20), (10,))
text(ax, f1(10), 56 + 11, '10·1 ≠ 0', 'varie', 's')
f2 = barre(22, 'autre', 'ℤ/2 ⊕ ℤ/10 : on ajoute (1, 1)', (0, 10, 20), ())
text(ax, f2(10), 22 + 11, '10·(1, 1) = (0, 0)', 'resultat', 's')
text(ax, 82, 56, 'k', 'fixe', 's')
text(ax, 82, 22, 'k', 'fixe', 's')
save(fig, '59-126')
