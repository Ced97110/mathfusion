import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
d = -18  # décalage vertical : la figure est resserrée, positions relatives inchangées
rows = [([39, 49], ['1', '1'], 72, 'sujet', 'normal'),
        ([34, 44, 54], ['1', '2', '1'], 62, 'sujet', 'normal'),
        ([29, 39, 49, 59], ['1', '3', '3', '1'], 52, 'sujet', 'normal'),
        ([24, 34, 44, 54, 64], ['1', '4', '6', '4', '1'], 42, 'sujet', 'normal'),
        ([19, 29, 39, 49, 59, 69], ['1', '5', '10', '10', '5', '1'], 30, 'resultat', 'bold')]
for xs, ss, y, r, w in rows:
    for x, s in zip(xs, ss):
        text(ax, x, y + d, s, r, 'm', weight=w)
a = [24, 34, 44, 54, 64]; b = [19, 29, 39, 49, 59, 69]
for k in range(4):
    arrow(ax, (a[k], 39.5 + d), (b[k + 1], 32.5 + d), 'varie')
    arrow(ax, (a[k + 1], 39.5 + d), (b[k + 1], 32.5 + d), 'varie')
arrow(ax, (24, 39.5 + d), (19, 32.5 + d), 'fixe')
arrow(ax, (64, 39.5 + d), (69, 32.5 + d), 'fixe')
ys = [72, 62, 52, 42, 30]
for k in range(4):
    arrow(ax, (80, ys[k] - 2 + d), (80, ys[k + 1] + 2 + d), 'varie', curve=0.4)
save(fig, '01-169')
