import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 20, 66, r'$D_4/\langle r\rangle$', 'sujet', 'm'); text(ax, 68, 66, r'$\mathbb{Z}/2\mathbb{Z}$', 'autre', 'm')
for y, a, b, ra, rb in [(54, 'R', '0', 'sujet', 'autre'), (38, 'S', '1', 'sujet', 'autre')]:
    box(ax, 12, y - 5, 16, 10, ra, label=a, size='l'); box(ax, 60, y - 5, 16, 10, rb, label=b, size='l')
    arrow(ax, (29, y), (59, y), 'resultat', both=True)
text(ax, 44, 46, 'même table (indice 2)', 'resultat', 's')
box(ax, 4, 3, 80, 26, 'limite', r=1.2)
text(ax, 44, 23.5, r'$D_4/\{1,\,r^2\}$ : 8 ÷ 2 = 4 éléments', 'limite', 's')
for i in range(4): disc(ax, 20 + 16 * i, 15, 3.8, 'limite')
text(ax, 44, 7, r'pas la table de $\mathbb{Z}/2\mathbb{Z}$', 'limite', 's')
save(fig, '47-158')
