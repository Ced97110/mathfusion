import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
steps = [r'$\alpha+(\alpha+1)$', r'$(1+1)\alpha+1$', r'$0+1$', r'$1$']
notes = [r'on regroupe les $\alpha$', r'règle 1 : $1+1=0$', r'$0+1=1$']
roles = ['sujet', 'varie', 'varie', 'resultat']
for i in range(4):
    y = 80 - 20 * i
    box(ax, 6, y, 42, 11, roles[i], label=steps[i], size='m')
    if i < 3:
        arrow(ax, (27, y), (27, y - 9), 'varie')
        text(ax, 32, y - 4.5, notes[i], 'varie', 's', ha='left')
text(ax, 44, 7, r'pour tout $a$ : $a+a=0$', 'encre', 'm')
save(fig, '67-015')
