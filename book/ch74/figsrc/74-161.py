import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 6, 58, 32, 9, 'sujet', label='p4m', size='l')
box(ax, 50, 58, 32, 9, 'autre', label='p4g', size='l')
box(ax, 22, 36, 44, 10, 'resultat', label=r'$D_4$ : 8 éléments', size='l')
arrow(ax, (22, 58), (36, 46.5), 'fixe')
arrow(ax, (66, 58), (52, 46.5), 'fixe')
text(ax, 44, 52.5, 'même groupe', 'fixe', 's')
x0 = 6.5
for i in range(8):
    role = 'varie' if i < 4 else 'autre'
    box(ax, x0 + i * 9.4, 17, 8.6, 8.6, role, label=['0°', '90°', '180°', '270°'][i] if i < 4 else None, size='s', r=0.5)
brace(ax, x0, x0 + 4 * 9.4 - 0.8, 16, 'varie', '4 rotations')
brace(ax, x0 + 4 * 9.4, x0 + 8 * 9.4 - 0.8, 16, 'autre', '4 réflexions')
arrow(ax, (44, 36), (44, 27.5), 'fixe')
save(fig, '74-161')
