import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 14, 62, 60, 14, 'sujet', label=r'$f=x^3-2$ dans $F[x]$', size='m')
text(ax, 44, 57, 'degré 3, coefficient dominant 1', 'sujet', 's')
box(ax, 2, 4, 84, 46, 'autre')
text(ax, 44, 45, r'$E=F(r_1,r_2,r_3)$', 'autre', 'm')
box(ax, 6, 8, 22, 26, 'fixe', label=r'$F=\mathbb{Q}$', size='m')
for i in range(3):
    x = 48 + i * 16
    disc(ax, x, 21, 5.5, 'sujet', label=f'$r_{i + 1}$', size='m')
    arrow(ax, (44 + i * 4 + 6, 55), (x, 27), 'sujet', lw=0.8)
text(ax, 64, 11.5, '3 racines distinctes', 'sujet', 's')
save(fig, '65-021')
