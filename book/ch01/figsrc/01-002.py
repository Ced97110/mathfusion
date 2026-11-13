import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
rows = [5, 4, 3, 2]
for r, n in enumerate(rows):
    for i in range(n):
        box(ax, 18 - (3.8 * n - 0.4) / 2 + 3.8 * i, 14 + 3.8 * r, 3.4, 3.4, 'fixe', r=0.3, lw=0.6)
        disc(ax, 70 + 3.8 * (i - (n - 1) / 2), 15.7 + 3.8 * r, 1.7, 'autre', lw=0.6)
text(ax, 18, 9, 'boîtes', 'fixe', 's')
text(ax, 70, 9, 'pommes', 'autre', 's')
arrow(ax, (32, 20), (56, 20), 'varie', both=True)
text(ax, 44, 23.5, 'échange', 'varie', 's')
text(ax, 44, 4, 'les objets changent', 'varie', 's')
box(ax, 36, 46, 16, 12, 'sujet', label='14', size='l')
text(ax, 44, 42.5, 'taille commune', 'sujet', 's')
line(ax, [(18, 30.5), (37, 46)], 'sujet', dash=True)
line(ax, [(70, 30.5), (51, 46)], 'sujet', dash=True)
text(ax, 44, 64, 'le nombre reste 14', 'resultat', 'm')
save(fig, '01-002')
