import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
def mp(x, y, parts, merged):
    for s, w, m in parts:
        box(ax, x, y, w, 10, 'varie' if m else 'sujet', label=s, size='s'); x += w
mp(29, 68, [('A', 10, 0), ('B', 10, 0), ('C', 10, 0)], 0)
mp(4, 40, [('AB', 20, 1), ('C', 10, 0)], 0); mp(54, 40, [('A', 10, 0), ('BC', 20, 1)], 0)
mp(29, 10, [('ABC', 30, 1)], 0)
arrow(ax, (36, 66), (19, 52), 'fixe'); arrow(ax, (52, 66), (69, 52), 'fixe')
arrow(ax, (19, 38), (36, 22), 'fixe'); arrow(ax, (69, 38), (52, 22), 'fixe')
text(ax, 15, 60, 'efface A|B', 'fixe', 's'); text(ax, 73, 60, 'efface B|C', 'fixe', 's')
text(ax, 15, 29, 'efface B|C', 'fixe', 's'); text(ax, 73, 29, 'efface A|B', 'fixe', 's')
save(fig, '80-380')
