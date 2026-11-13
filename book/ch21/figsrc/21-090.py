import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
steps = [(r'$4(x+6)=2(x-1)$', 'sujet'), (r'$4x+24=2x-2$', 'sujet'), (r'$2x+24=-2$', 'sujet'),
         (r'$2x=-26$', 'sujet'), (r'$x=-13$', 'resultat')]
acts = ['développer', 'retirer 2x', 'retirer 24', 'diviser par 2']
for i, (e, role) in enumerate(steps):
    y = 86 - i * 20
    box(ax, 4, y, 46, 10, role, True, e)
    if i < 4:
        arrow(ax, (27, y - 0.5), (27, y - 9.5), 'varie')
        text(ax, 32, y - 5, acts[i], 'varie', 's', ha='left')
save(fig, '21-090')
