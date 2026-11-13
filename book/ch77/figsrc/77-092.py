import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
c = 9; x0 = 22; ytop = 44
heads = [r'$u\cdot1$', r'$u\cdot i$', r'$u\cdot j$', r'$u\cdot k$']
for j in range(4):
    text(ax, x0 + (j + 0.5) * c, ytop + 4, heads[j], 'encre', 's')
for i in range(4):
    for j in range(4):
        if i == j:
            box(ax, x0 + j * c, ytop - (i + 1) * c, c, c, 'sujet', label=r'$a_0$', size='m', r=0.4, lw=0.6)
        else:
            box(ax, x0 + j * c, ytop - (i + 1) * c, c, c, 'fixe', r=0.4, lw=0.4)
text(ax, 11, ytop - 2 * c, 'diagonale', 'sujet', 's', rot=90)
text(ax, 44, 6, r'$T(u)=a_0+a_0+a_0+a_0=4a_0$', 'sujet', 'm')
save(fig, '77-092')
