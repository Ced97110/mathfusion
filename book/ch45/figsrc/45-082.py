import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
bw, gap, x0 = 12, 4, 28
for i in range(4):
    x = x0 + i * (bw + gap)
    box(ax, x, 36, bw, 9, 'fixe', label=str(i))
    box(ax, x, 14, bw, 9, 'sujet', label=str((2 + i) % 4))
    arrow(ax, (x + bw / 2, 35.5), (x + bw / 2, 23.5), 'varie')
text(ax, 14, 40.5, r'$x$', 'fixe', 'l')
text(ax, 14, 18.5, r'$a_L(x)$', 'sujet', 'l')
text(ax, 14, 29.5, r'$2+x$', 'varie', 'm')
brace(ax, x0, x0 + 4 * bw + 3 * gap, 12, 'sujet', label='ligne de 2 de la table')
save(fig, '45-082')
