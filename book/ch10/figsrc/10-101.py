import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = lambda v: 8 + (v - 100) / 40 * 64
line(ax, [(8, 30), (82, 30)], 'fixe')
text(ax, 44, 56, 'totaux possibles', 'sujet', 'm')
for i, v in enumerate(range(100, 141, 10)):
    disc(ax, f(v), 30, 1.5, 'sujet'); text(ax, f(v), 24, str(v), 'sujet', 's')
    if i < 4:
        arrow(ax, (f(v) + 1.5, 32), (f(v + 10) - 1.5, 32), 'varie', curve=-0.5, lw=0.8)
        text(ax, (f(v) + f(v + 10)) / 2, 41, '+10', 'varie', 's')
disc(ax, f(116), 30, 1.8, 'limite', fill=False)
text(ax, f(116), 10, '116 voulu', 'limite', 'm', weight='bold')
arrow(ax, (f(116), 13), (f(116), 27.8), 'limite', lw=0.8)
save(fig, '10-101')
