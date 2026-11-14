import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cw, gap, x0 = 7.2, 1.2, 4.0
yb, h = 8, 40
for r in range(10):
    x = x0 + r * (cw + gap)
    hl = (r == 7)
    box(ax, x, yb, cw, h, 'sujet' if hl else 'fixe', r=1.0)
    text(ax, x + cw / 2, yb + h + 4, str(r), 'sujet' if hl else 'fixe', 's', weight='bold' if hl else 'normal')
    for k in range(3):
        yy = yb + h - 7 - k * 11
        if hl:
            text(ax, x + cw / 2, yy, str(r + 10 * k), 'sujet', 's')
        else:
            disc(ax, x + cw / 2, yy, 1.3, 'fixe')
text(ax, 44, 60, 'ℤ/(10) : dix rangements', 'sujet', 'm')
save(fig, '59-104')
