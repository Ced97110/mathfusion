import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
y0 = 30.0
f = numberline(ax, 8, 72, y0, -4, 8, 1, labels=False)
for v in range(1, 9):
    disc(ax, f(v), y0, 1.2, 'sujet')
for v in (0, -3):
    disc(ax, f(v), y0, 1.2, 'limite', fill=False)
for v, s, role in [(-3, '−3', 'limite'), (0, '0', 'limite'), (3, '3', 'sujet'), (5, '5', 'sujet'), (8, '8', 'resultat')]:
    text(ax, f(v), y0 - 5, s, role, 's')
arrow(ax, (f(3) - 0.5, y0 + 2), (f(0) + 0.5, y0 + 2), 'varie', curve=0.5)
arrow(ax, (f(3) - 0.5, y0 + 2), (f(-3) + 0.5, y0 + 2), 'varie', curve=0.4)
text(ax, f(1.5), y0 + 8.5, r'$\times 0$', 'varie', 's')
text(ax, f(-1.5), y0 + 11.5, r'$\times(-1)$', 'varie', 's')
arrow(ax, (f(3) + 0.5, y0 - 8), (f(8) - 0.5, y0 - 8), 'resultat', curve=0.2)
text(ax, f(5.5), y0 - 14.5, r'$+\,5$ : reste dedans', 'resultat', 's')
text(ax, 44, 54, 'entiers > 0 : stable par +', 'sujet', 'm')
text(ax, f(0), y0 - 9.5, r'$\notin$', 'limite', 's')
text(ax, f(-3), y0 - 9.5, r'$\notin$', 'limite', 's')
save(fig, '57-125')
