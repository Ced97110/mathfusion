import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
for x, role, t in [(3, 'sujet', 'addition'), (46, 'autre', 'multiplication')]:
    box(ax, x, 36, 39, 24, role)
    text(ax, x + 19.5, 54, t, role, 'l', weight='bold')
    text(ax, x + 19.5, 46, 'commutativité', role, 's')
    text(ax, x + 19.5, 41, 'associativité', role, 's')
box(ax, 3, 4, 82, 20, 'varie')
text(ax, 44, 19, 'distributivité', 'varie', 'l', weight='bold')
text(ax, 44, 10.5, r'$4(5+2)=4\cdot5+4\cdot2$', 'varie', 'm')
arrow(ax, (22.5, 24.8), (22.5, 35.2), 'varie'); arrow(ax, (65.5, 24.8), (65.5, 35.2), 'varie')
text(ax, 44, 30, 'mélange + et ×', 'varie', 's')
save(fig, '12-102')
