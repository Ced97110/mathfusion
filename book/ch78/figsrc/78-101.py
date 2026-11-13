import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 18, 60, 'une formule par nombre', 'fixe', 's')
for k, v in enumerate(['−1', '2', '−3']):
    box(ax, 4, 42 - k * 13, 24, 9, 'fixe', label=f'$c={v}$'.replace('−', '-'))
text(ax, 68, 60, 'une formule pour tous', 'sujet', 's')
box(ax, 54, 36, 28, 14, 'sujet', label=r'$c$', size='xl')
for k in range(3):
    arrow(ax, (29, 46.5 - k * 13), (53, 43), 'varie')
box(ax, 54, 18, 28, 9, 'resultat', label=r'$c\neq0$')
text(ax, 68, 9, r'réels : $c=-1$', 'varie', 's')
save(fig, '78-101')
