import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
s = 30.0; x0, y0 = 10, 14
A, B, C, D = (x0, y0), (x0+s, y0), (x0+s, y0+s), (x0, y0+s)
poly(ax, [A, B, C, D], 'sujet')
line(ax, [A, C], 'encre', lw=1.4, dash=True)
for p, n, dx, dy in ((A, 'A', -3.5, -3.5), (B, 'B', 3.5, -3.5), (C, 'C', 3.5, 3.5), (D, 'D', -3.5, 3.5)):
    disc(ax, p[0], p[1], 1.2, 'sujet')
    text(ax, p[0]+dx, p[1]+dy, n, 'sujet', 'l', weight='bold')
text(ax, 64, 42, 'A, B, C, D :\nles 4 sommets', 'sujet', 'm')
text(ax, 64, 22, 'segment AC :\nde A à C', 'encre', 'm')
save(fig, '22-013')
