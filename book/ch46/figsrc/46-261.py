import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
f = numberline(ax, 8, 80, 14, -1, 6, step=1, arrow_right=False)
for v in range(-1, 7):
    if v % 2: disc(ax, f(v), 14, 1.7, 'sujet')
    else: disc(ax, f(v), 14, 1.7, 'limite', fill=False)
arrow(ax, (f(3), 17), (f(1), 17), 'varie', curve=-0.0 + 0.6)
text(ax, f(2), 28, '3 − 1 = 2', 'varie', 'l')
text(ax, 44, 42, 'entiers impairs', 'sujet', 'm')
text(ax, 44, 3, '2 et 0 sont pairs : hors de l’ensemble', 'limite', 's')
save(fig, '46-261')
