import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
cw = 12; x0 = 52; ytop = 36
text(ax, 20, 44, r'$c=3$, base $(1,\,i)$', 'sujet', 'm')
text(ax, 20, 33, r'$1\mapsto3\cdot1$', 'varie', 'm')
text(ax, 20, 20, r'$i\mapsto3\cdot i$', 'varie', 'm')
vals = [['3', '0'], ['0', '3']]
for i in range(2):
    for j in range(2):
        box(ax, x0 + j * cw, ytop - (i + 1) * cw, cw, cw, 'sujet' if i == j else 'fixe', label=vals[i][j], size='l', r=0.4, lw=0.6)
arrow(ax, (34, 33), (x0 - 1, ytop - 0.5 * cw), 'varie')
arrow(ax, (34, 20), (x0 + 1.5 * cw, ytop - 2 * cw - 1.5), 'varie', curve=0.3)
text(ax, x0 + cw, ytop + 4, r'$\rho(3)=3\cdot1$', 'sujet', 's')
text(ax, 44, 5, r'$c$ sur la diagonale, 0 ailleurs', 'encre', 's')
save(fig, '77-093')
