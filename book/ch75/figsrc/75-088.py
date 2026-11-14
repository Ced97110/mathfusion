import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, r'$Sp$ : 51 840 éléments', 'sujet', 'm')
n = 5; xs = [14 + i * 15 for i in range(n)]
for i, x in enumerate(xs):
    disc(ax, x - 3.5, 46, 2.6, 'sujet'); disc(ax, x + 3.5, 46, 2.6, 'sujet')
    box(ax, x - 7, 42, 14, 8, 'varie', fill=False, dash=True)
    arrow(ax, (x, 41), (x, 29), 'varie', lw=1.0)
    disc(ax, x, 25, 3, 'resultat')
text(ax, 14 - 3.5, 53.5, r'$\eta$', 'sujet', 's'); text(ax, 14 + 4.5, 53.5, r'$-\eta$', 'sujet', 's')
text(ax, 44, 14, r'$PSp$ : 25 920 éléments', 'resultat', 'm')
text(ax, 44, 6, '51 840 : 2 = 25 920', 'encre', 's')
save(fig, '75-088')
