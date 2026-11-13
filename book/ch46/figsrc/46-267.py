import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
f = numberline(ax, 8, 70, 16, -3, 4, step=1, arrow_right=True)
for v in range(-3, 5):
    if v >= 1: disc(ax, f(v), 16, 1.7, 'sujet')
    elif v == -1: disc(ax, f(v), 16, 1.7, 'limite', fill=False)
arrow(ax, (f(1), 19), (f(3), 19), 'varie', curve=-0.6)
text(ax, f(2), 31, '1 + 2 = 3 : reste dedans', 'resultat', 's')
text(ax, 44, 44, 'entiers positifs 1, 2, 3, …', 'sujet', 'm')
text(ax, f(-1), 7, '−1 n’y est pas', 'limite', 's')
save(fig, '46-267')
