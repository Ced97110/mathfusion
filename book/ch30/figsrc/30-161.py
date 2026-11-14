import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
ry = 46
line(ax, [(2, ry), (86, ry)], 'fixe', dash=True)
text(ax, 3, ry + 2.2, 'repos', 'fixe', 's', ha='left')
for x, a in [(26, 5), (64, 13)]:
    h = a * 2.4
    disc(ax, x, ry + h, 3.5, 'fixe', fill=False)
    disc(ax, x, ry - h, 3.5, 'fixe', fill=False)
    arrow(ax, (x, ry - h + 3.5), (x, ry + h - 3.5), 'sujet', both=True)
    text(ax, x, ry + h + 6.5, f'+{a}', 'fixe', 's')
    text(ax, x, ry - h - 6.5, f'−{a}', 'fixe', 's')
    text(ax, x + 3, ry + 4, f'a = {a}', 'sujet', 'm', ha='left')
save(fig, '30-161')
