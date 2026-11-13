import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
data = [(50, 'fixe', '$(x+2)$', '$(x+3)$', 'ordinaire\ndifférentes'),
        (32, 'sujet', '$(x+3)$', '$(x+3)$', 'remarquable\nidentiques'),
        (14, 'autre', '$(x+3)$', '$(x-3)$', 'remarquable\nsigne opposé')]
for y, role, a, b, lab in data:
    box(ax, 4, y, 24, 12, role, label=a); box(ax, 32, y, 24, 12, role, label=b)
    text(ax, 60, y + 6, lab, role, 's', ha='left')
save(fig, '15-096')
