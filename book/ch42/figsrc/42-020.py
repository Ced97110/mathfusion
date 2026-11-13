import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 4, 14, 52, 34, 'fixe')
text(ax, 9, 44, 'le sac', 'fixe', 's', ha='left')
for x, t in [(8, 'gourde'), (32, 'carte')]:
    box(ax, x, 22, 20, 10, 'sujet', label=t, size='s')
    text(ax, x + 10, 39, 'élément', 'sujet', 's')
    arrow(ax, (x + 10, 37), (x + 10, 33.5), 'sujet')
brace(ax, 4, 56, 14, 'sujet', label='2 éléments')
box(ax, 64, 22, 20, 10, 'fixe', fill=False, dash=True, label='lampe', size='s')
text(ax, 74, 39, 'pas dedans', 'limite', 's')
save(fig, '42-020')
