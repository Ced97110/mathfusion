import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 22, 60, 44, 9, 'sujet', label='sin θ = 23/37 = 0,6216…')
cols = [(2, 'limite', 'arrondir d\'abord', '0,622', '38,46°'), (48, 'resultat', 'garder tout', '0,6216…', '38,43°')]
for x, role, title, val, ang in cols:
    text(ax, x + 19, 53, title, role, 'm', weight='bold')
    box(ax, x, 38, 38, 9, role, label=val)
    arrow(ax, (x + 19, 38), (x + 19, 27), role)
    text(ax, x + 20.5, 32.5, 'arcsin', role, 's', ha='left')
    box(ax, x, 16, 38, 10, role, label=ang, size='l')
    arrow(ax, (x + 19, 60), (x + 19, 47.8), 'fixe') if False else None
arrow(ax, (30, 60), (21, 47.5), 'fixe'); arrow(ax, (58, 60), (67, 47.5), 'fixe')
arrow(ax, (40.5, 21), (47.5, 21), 'varie', both=True)
text(ax, 44, 11, 'écart 0,03°', 'varie', 's')
save(fig, '26-081')
