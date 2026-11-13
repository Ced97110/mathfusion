import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
text(ax, 44, 70, r'$|\mathrm{Stab}| = 2$ pour chaque point', 'sujet', 's')
for i, n in enumerate('ABCD'):
    cx = 14 + i * 20
    box(ax, cx - 6, 28, 12, 10, 'sujet', r=0.3); box(ax, cx - 6, 38, 12, 10, 'sujet', r=0.3)
    text(ax, cx, 20, n, 'resultat', 'm')
line(ax, [(4, 52), (84, 52)], 'fixe', dash=True)
text(ax, 44, 58, 'même hauteur', 'fixe', 's')
text(ax, 44, 8, r'$8 \div 4 = 2$', 'encre', 'l')
save(fig, '49-175')
