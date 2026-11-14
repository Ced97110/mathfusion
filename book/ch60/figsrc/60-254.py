import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 21, 71, 'chapitre 23', 'fixe', 's')
text(ax, 21, 64, 'discriminant = 0', 'sujet', 's')
ay = 36
line(ax, [(4, ay), (38, ay)], 'fixe')
pts = [(21 + x * 9, ay + x * x * 6) for x in [i / 20 * 3 - 1.5 for i in range(21)]]
line(ax, pts, 'sujet', lw=1.1)
disc(ax, 21, ay, 1.4, 'varie')
text(ax, 21, 30, 'racine double', 'varie', 's')
text(ax, 68, 71, 'polynôme minimal', 'fixe', 's')
text(ax, 68, 64, r'racine double de $m$', 'sujet', 's')
c = 9
for i, row in enumerate([['r', '1'], ['0', 'r']]):
    for j, v in enumerate(row):
        role = 'sujet' if v == 'r' else ('varie' if v == '1' else 'fixe')
        box(ax, 59 + j * c, 44 - i * c, c - 0.8, c - 0.8, role, label=v)
text(ax, 68, 30, r'bloc de taille $\geq2$', 'varie', 's')
arrow(ax, (41, 45), (49, 45), 'varie', both=True)
text(ax, 45, 50, 'signal', 'varie', 's')
save(fig, '60-254')
