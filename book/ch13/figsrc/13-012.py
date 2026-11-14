import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = numberline(ax, 8, 74, 20, -4, 4, labels=False)
for v in range(-4, 5): text(ax, f(v), 16.4, str(v).replace('-', '−'), 'fixe', 's')
line(ax, [(f(0), 20), (f(0), 44)], 'fixe', dash=True)
disc(ax, f(3), 20, 2.4, 'sujet'); disc(ax, f(-3), 20, 2.4, 'varie')
for v, r in [(3, 'sujet'), (-3, 'varie')]:
    line(ax, [(f(v), 22.4), (f(v), 28)], r, lw=0.5, dash=True)
    text(ax, f(v), 24.5, 'P' if v > 0 else 'Q', r, 's', ha='center')
arrow(ax, (f(0) + 0.8, 28), (f(3), 28), 'sujet'); arrow(ax, (f(0) - 0.8, 28), (f(-3), 28), 'varie')
text(ax, (f(0) + f(3)) / 2, 33, '3 pas', 'sujet', 'm'); text(ax, (f(0) + f(-3)) / 2, 33, '3 pas', 'varie', 'm')
save(fig, '13-012')
