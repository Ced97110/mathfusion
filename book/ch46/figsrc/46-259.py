import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 32, 40, 24, 10, 'fixe', label='(1)', size='l')
text(ax, 44, 55, 'neutre : ne rien bouger', 'fixe', 's')
xs = [6, 32, 58]; ws = [24, 24, 26]
labs = ['(4 5)', '(1 3)', '(1 3)(4 5)']
for x, wd, s in zip(xs, ws, labs):
    box(ax, x, 8, wd, 10, 'sujet', label=s, size='m')
    cx = x + wd / 2
    arrow(ax, (cx, 19.5), (44 + (cx - 44) * 0.3, 38.5), 'varie', curve=0.0)
text(ax, 44, 29, 'deux fois : tout en place', 'varie', 's')
text(ax, 44, 2.5, 'trois éléments d’ordre 2', 'sujet', 's')
save(fig, '46-259')
