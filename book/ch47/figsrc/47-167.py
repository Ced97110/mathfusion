import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 20, 66, r'$S_3$ : 6', 'encre', 'm'); text(ax, 68, 66, 'quotient : 2', 'encre', 'm')
L = [('1', 'sujet'), ('(1 2 3)', 'sujet'), ('(1 3 2)', 'sujet'), ('(1 2)', 'varie'), ('(1 3)', 'varie'), ('(2 3)', 'varie')]
for i, (l, r) in enumerate(L):
    y = 54 - i * 9.5
    box(ax, 3, y - 4, 24, 8, r, label=l, size='s')
    ty = 44 if i < 3 else 20
    arrow(ax, (27.5, y), (56, ty + (i % 3 - 1) * 3.5), r)
box(ax, 56, 36, 28, 16, 'sujet', label='paire', size='m')
box(ax, 56, 12, 28, 16, 'varie', label='impaire', size='m')
text(ax, 70, 6, 'on garde la parité', 'resultat', 's')
save(fig, '47-167')
