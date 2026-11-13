import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 70, 'on compte les papiers : 500', 'fixe', 'm')
for i in range(12): box(ax, 4 + i * 6.9, 52, 5.6, 11, 'fixe', r=0.3)
arrow(ax, (44, 49), (44, 40), 'varie', lw=1.2)
roles = ['sujet', 'varie', 'autre']
for g in range(3):
    x0 = 4 + g * 28.2
    box(ax, x0, 8, 25.6, 28, roles[g], fill=False, dash=True, lw=1.0)
    for k in range(4): box(ax, x0 + 1.9 + k * 5.7, 19, 4.6, 11, roles[g], r=0.3)
    text(ax, x0 + 12.8, 12.5, 'une façon', roles[g], 's')
text(ax, 48, 44.5, 'on compte les façons', 'varie', 'm', ha='left')
save(fig, '74-002')
