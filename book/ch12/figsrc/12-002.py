import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
y = 20
f = numberline(ax, 8, 70, y, 0, 40, step=5, arrow_right=False)
box(ax, 30, 38, 16, 10, 'sujet', label=r'$x$', size='xl')
for v in (10, 25, 35):
    disc(ax, f(v), y, 1.7, 'varie')
    arrow(ax, (38, 38), (f(v), y + 2.6), 'sujet')
brace(ax, f(0), f(36), y - 6, 'resultat', label=r'$x < 36$ : vrai pour les 3')
save(fig, '12-002')
