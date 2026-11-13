import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 20, 74, 'plan réel', 'fixe', 's')
O = (20, 40)
line(ax, [(O[0] - 17, O[1]), (O[0] + 17, O[1])], 'varie', lw=1.3)
line(ax, [(O[0], O[1] - 17), (O[0], O[1] + 17)], 'varie', lw=1.3)
line(ax, [(O[0] - 14, O[1] - 14), (O[0] + 14, O[1] + 14)], 'varie', lw=1.3)
disc(ax, *O, 1.6, 'fixe')
text(ax, 31, 35.5, r'$Fx$', 'varie', 's'); text(ax, 15, 56, r'$Fy$', 'varie', 's'); text(ax, 32, 56, r'$F(x+y)$', 'varie', 's')
text(ax, 66, 74, 'diamant', 'fixe', 's')
top, bot = (66, 62), (66, 14)
mids = [(52, 38, r'$Fx$'), (66, 38, r'$Fy$'), (80, 38, r'$F(x+y)$')]
for x, y, l in mids:
    line(ax, [(66, 22), (x, y - 4)]); line(ax, [(x, y + 4), (66, 54)])
for x, y, l in mids:
    box(ax, x - 6.5, y - 4, 13, 8, 'varie', label=l, size='s')
box(ax, 58, 54, 16, 8, 'resultat', label='plan', size='s'); box(ax, 58, 14, 16, 8, 'resultat', label=r'$0$', size='s')
save(fig, '79-155')
