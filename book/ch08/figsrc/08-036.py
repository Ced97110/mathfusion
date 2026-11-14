import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
f = numberline(ax, 8, 78, 14, 0, 1, step=0.1, every=10, arrow_right=False)
disc(ax, f(0.7), 14, 1.5, 'sujet'); disc(ax, f(0.07), 14, 1.5, 'varie')
text(ax, f(0.7), 22, '0,7', 'sujet', 'l'); text(ax, f(0.07), 22, '0,07', 'varie', 'l')
arrow(ax, (f(0.7) - 2, 34), (f(0.07) + 2, 34), 'limite')
text(ax, 44, 40, '10 fois plus petit', 'limite', 'm')
text(ax, 44, 50, 'un zéro de plus après la virgule', 'fixe', 's') if False else text(ax, 44, 50, 'un zéro de plus : 7 change de place', 'fixe', 's') if False else None
save(fig, '08-036')
