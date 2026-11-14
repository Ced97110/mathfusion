import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
gx = lambda x: 4 + x * 6; gy = lambda y: 10 + y * 5.5
line(ax, [(gx(0), gy(0)), (gx(5), gy(0))]); line(ax, [(gx(0), gy(0)), (gx(0), gy(4))])
line(ax, [(gx(0), gy(1/3)), (gx(5), gy(2/3*5+1/3))], 'sujet', lw=1.2)
disc(ax, gx(1), gy(1), 1.1, 'sujet'); disc(ax, gx(4), gy(3), 1.1, 'autre')
text(ax, gx(1) + 1, gy(1) + 4, r'$A$', 'sujet', 'm'); text(ax, gx(4) - 3.5, gy(3) + 3, r'$B$', 'autre', 'm')
text(ax, 18, 57, 'deux points connus', 'sujet', 's')
for y, r, s in [(44, 'varie', r'1  pente $\frac{2}{3}$'), (26, 'fixe', r'2  $y-1=\frac{2}{3}(x-1)$'), (8, 'resultat', r'3  $y=\frac{2}{3}x+\frac{1}{3}$')]:
    box(ax, 42, y, 44, 13, r, label=s)
arrow(ax, (64, 44), (64, 39.5), 'varie'); arrow(ax, (64, 26), (64, 21.5), 'varie')
text(ax, 64, 62, 'trois actions', 'encre', 's')
save(fig, '19-103')
