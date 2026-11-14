import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 2, 50, 84, 32, 'sujet', lw=1.1)
text(ax, 44, 76, r'$E(2)$ : tous les $Ax+b$', 'sujet', 'm')
for i in range(14):
    for j in range(2):
        disc(ax, 8 + i * 5.6, 66 - j * 6, 1.1, 'sujet')
text(ax, 44, 54, 'une infinité …', 'sujet', 's')
poly(ax, [(70, 22), (82, 22), (82, 34), (70, 34)], 'autre')
text(ax, 76, 38, r'$X$ : carré', 'autre', 's')
arrow(ax, (30, 49), (30, 36), 'varie', lw=1.4)
text(ax, 54, 43, 'on fixe le carré', 'varie', 's')
box(ax, 2, 4, 56, 32, 'resultat', lw=1.1)
text(ax, 30, 30, r'Sym($X$) : 8 éléments', 'resultat', 's')
for k in range(8):
    disc(ax, 12 + k * 5.2, 15, 1.6, 'resultat')
save(fig, '74-106')
