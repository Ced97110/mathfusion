import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 4, 68, 80, 11, 'sujet', label=r'départ : $H$ ≠ {$e$}', size='m')
arrow(ax, (44, 68), (44, 61), 'fixe')
box(ax, 4, 49, 80, 12, 'varie', label=r'étape clé : $s$ = plus petit > 0', size='m', weight='bold')
arrow(ax, (44, 49), (44, 42), 'fixe')
box(ax, 4, 31, 80, 11, 'resultat', label=r'arrivée : $H=\langle a^{s}\rangle$', size='m')
f = numberline(ax, 12, 76, 14, 0, 12, step=3, labels=False, arrow_right=False)
for v in (0, 3, 6, 9):
    disc(ax, f(v), 14, 1.8, 'varie' if v == 3 else 'sujet')
    text(ax, f(v), 8, str(v), 'varie' if v == 3 else 'sujet', 's')
text(ax, f(3), 20.5, r'$s$ = 3', 'varie', 's')
text(ax, 44, 26, 'sur l’horloge : 0, 3, 6, 9', 'fixe', 's')
save(fig, '46-120')
