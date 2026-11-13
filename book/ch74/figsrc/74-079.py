import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 2, 48, 'bande 1', 'sujet', 's', ha='left'); text(ax, 2, 31, 'bande 2', 'autre', 's', ha='left')
for i in range(4):
    text(ax, 26 + 7*i, 48, 'bp'[i % 2], 'sujet', 'l'); text(ax, 26 + 17.5*i, 31, 'bp'[i % 2], 'autre', 'l')
arrow(ax, (26, 53), (33, 53), 'varie', both=True); text(ax, 29.5, 57, '2 cm', 'varie', 's')
arrow(ax, (26, 36), (43.5, 36), 'varie', both=True); text(ax, 34.75, 40.5, '5 cm', 'varie', 's')
box(ax, 8, 6, 72, 12, 'resultat', label=r'même $G_0$ : tourner, retourner', size='m')
save(fig, '74-079')
