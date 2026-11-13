import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
s = 30.0; x0, y0 = 10, 14
A, B, C, D = (x0, y0), (x0+s, y0), (x0+s, y0+s), (x0, y0+s)
poly(ax, [A, B, C, D], 'sujet')
line(ax, [A, C], 'encre', lw=2.0)
for p, n, dx, dy in ((A, 'A', -3.5, -3.5), (B, 'B', 3.5, -3.5), (C, 'C', 3.5, 3.5), (D, 'D', -3.5, 3.5)):
    disc(ax, p[0], p[1], 1.2, 'sujet')
    text(ax, p[0]+dx, p[1]+dy, n, 'sujet', 'm')
text(ax, x0 + s/2 + 4, y0 + s/2 - 4, r'$d$', 'encre', 'xl', weight='bold')
text(ax, 64, 38, r'$d$ : longueur' + '\nde A à C', 'encre', 'm')
text(ax, 64, 20, 'inconnue, mais\non lui donne\nune lettre', 'fixe', 's')
save(fig, '22-014')
