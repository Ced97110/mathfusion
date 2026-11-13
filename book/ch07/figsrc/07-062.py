import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
for x, a, b, w in ((16, '3', '4', 12), (72, '12', '5', 12)):
    box(ax, x - w / 2, 36, w, 9, 'sujet', label=a, size='l')
    box(ax, x - w / 2, 15, w, 9, 'sujet', label=b, size='l')
    line(ax, [(x - 8, 30), (x + 8, 30)], 'encre', lw=1.4)
text(ax, 44, 40.5, 'haut : entier', 'fixe', 'm'); text(ax, 44, 19.5, 'bas : entier', 'fixe', 'm')
arrow(ax, (33, 40.5), (24, 40.5), 'fixe', lw=0.8); arrow(ax, (55, 40.5), (64, 40.5), 'fixe', lw=0.8)
arrow(ax, (33, 19.5), (24, 19.5), 'fixe', lw=0.8); arrow(ax, (55, 19.5), (64, 19.5), 'fixe', lw=0.8)
text(ax, 44, 6, 'deux nombres entiers', 'resultat', 'm')
save(fig, '07-062')
