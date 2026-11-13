import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
cw = 80 / 12
cx = lambda k: 4 + (k + 0.5) * cw
text(ax, 44, 71, 'entiers rangés par heure', 'encre', 'l')
text(ax, 44, 65.5, 'même colonne : écart de 12', 'fixe', 's')
for k in range(12):
    hot = (k == 2)
    box(ax, 4 + k * cw, 36, cw, 24, 'sujet' if hot else 'fixe', fill=hot, dash=not hot, lw=0.7, r=0.5)
    disc(ax, cx(k), 52, 1.7, 'sujet' if hot else 'fixe')
    disc(ax, cx(k), 45, 1.7, 'sujet' if hot else 'fixe')
    box(ax, 4 + k * cw, 12, cw, 7, 'sujet' if hot else 'resultat', lw=0.7, r=0.5)
    arrow(ax, (cx(k), 35.6), (cx(k), 19.6), 'varie' if hot else 'fixe', lw=0.7 if not hot else 1.1)
text(ax, cx(2), 57, '2', 'sujet', 's'); text(ax, cx(2), 40, '14', 'sujet', 's')
text(ax, cx(2) + 9, 8, 'heure 2', 'sujet', 's')
text(ax, 62, 28, r'$14-2=12\in K$', 'resultat', 'm')
save(fig, '59-037')
