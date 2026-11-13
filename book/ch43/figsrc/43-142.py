import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = numberline(ax, 8, 74, 28, 0, 5, arrow_right=True)
disc(ax, f(2), 28, 1.6, 'sujet'); disc(ax, f(3), 28, 1.6, 'autre')
arrow(ax, (f(2) + 1, 30), (f(3) - 1, 30), 'resultat', curve=-0.6)
text(ax, (f(2) + f(3)) / 2, 42, r'$2 \leq 3$ : vrai', 'resultat', 's')
arrow(ax, (f(3) - 1, 22), (f(2) + 1, 22), 'limite', curve=-0.6)
text(ax, (f(2) + f(3)) / 2, 10, r'$3 \leq 2$ : faux', 'limite', 's')
save(fig, '43-142')
