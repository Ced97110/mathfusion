import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, 'trois noms, une même forme', 'fixe', 's')
labs = ['couples\nde réels', "couples\nd'entiers", 'plan et\nquart de tour']
for x, s in zip([2, 31, 60], labs):
    box(ax, x, 32, 26, 16, 'sujet', label=s, size='s')
    arrow(ax, (x + 13, 32), (44 + (x + 13 - 44) * 0.35, 21), 'varie', lw=1.1)
box(ax, 24, 4, 40, 16, 'resultat', label='module', size='xl', weight='bold')
save(fig, '57-019')
