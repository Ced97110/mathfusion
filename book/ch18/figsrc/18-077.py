import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 19, 72, r'$20x^2$', 'sujet', 'l'); text(ax, 68, 72, r'$6$', 'autre', 'l')
L = [(r'$20x\cdot x$', 59), (r'$10x\cdot2x$', 45), (r'$5x\cdot4x$', 31)]
R = [(r'$6\cdot1$', 52), (r'$3\cdot2$', 36)]
for _, yl in L:
    for _, yr in R:
        if not (yl == 31 and yr == 36):
            line(ax, [(34, yl), (56, yr)], 'fixe', lw=0.6)
line(ax, [(34, 31), (56, 36)], 'resultat', lw=1.6)
for s, y in L: box(ax, 4, y - 5, 30, 10, 'sujet', label=s)
for s, y in R: box(ax, 56, y - 5, 24, 10, 'autre', label=s)
text(ax, 44, 14, r'garder : milieu $=23x$', 'resultat', 'm')
save(fig, '18-077')
