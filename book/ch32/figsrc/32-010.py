import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 4, 70, 24, 0, 24, step=1, labels=False, arrow_right=True)
for t in (1, 5, 13, 17):
    disc(ax, f(t), 24, 2.0, 'sujet' if t == 1 else 'resultat')
    text(ax, f(t), 30, f'{t} h', 'sujet' if t == 1 else 'resultat', 'm')
text(ax, 81, 24, '…', 'resultat', 'l')
text(ax, f(0), 18.5, '0 h', 'fixe', 's')
text(ax, f(24), 18.5, '24 h', 'fixe', 's')
text(ax, 40, 11, 'hauteur 3 m à ces heures', 'resultat', 'm')
box(ax, 18, 40, 52, 9, 'limite', label='« C’est fini » est faux')
save(fig, '32-010')
