import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
A = [['2', '1'], ['1', '3']]
for r in range(2):
    for c in range(2):
        box(ax, 7 + c * 13, 62 - r * 12, 12, 10, 'sujet', label=A[r][c], size='l', weight='bold')
line(ax, [(8.5, 75), (5.5, 75), (5.5, 51), (8.5, 51)], 'encre', lw=1.0)
line(ax, [(31.5, 75), (34.5, 75), (34.5, 51), (31.5, 51)], 'encre', lw=1.0)
text(ax, 39, 62, r'$\times$', 'encre', 'l', weight='bold')
box(ax, 43, 62, 12, 10, 'varie', label=r'$x_1$', size='l')
box(ax, 43, 50, 12, 10, 'varie', label=r'$x_2$', size='l')
text(ax, 60, 61, '=', 'encre', 'l', weight='bold')
box(ax, 65, 62, 14, 10, 'resultat', label='14', size='l', weight='bold')
box(ax, 65, 50, 14, 10, 'resultat', label='17', size='l', weight='bold')
text(ax, 30, 41, r'$2x_1+x_2=14$', 'fixe', 's')
text(ax, 66, 41, r'$x_1+3x_2=17$', 'fixe', 's')
arrow(ax, (44, 36), (44, 25), 'varie', lw=1.3)
box(ax, 18, 8, 52, 15, 'resultat', label=r'$(x_1,\ x_2)=(5,\ 4)$', size='m', weight='bold')
save(fig, '58-266')
