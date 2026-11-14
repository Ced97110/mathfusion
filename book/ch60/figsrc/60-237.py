import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
Z = lambda n: rf'\mathbb{{Z}}/{n}'
blocks = [('2', 2, [('2', Z(4)), ('1 + 1', Z(2) + r'\oplus' + Z(2))]),
          ('3', 3, [('3', Z(27)), ('2 + 1', Z(9) + r'\oplus' + Z(3)),
                    ('1 + 1 + 1', Z(3) + r'\oplus' + Z(3) + r'\oplus' + Z(3))]),
          ('5', 1, [('1', Z(5))])]
step = 10; y = 74
text(ax, 12, 84, 'premier', 'sujet', 's')
text(ax, 32, 84, 'partition', 'varie', 's')
text(ax, 62, 84, 'groupe', 'fixe', 's')
for p, e, groups in blocks:
    n = len(groups)
    box(ax, 3, y - (n - 1) * step - 4.5, 18, n * step - 1, 'sujet', label=rf'$p={p}$')
    for k, (part, g) in enumerate(groups):
        yy = y - k * step - 4.5
        box(ax, 23, yy, 19, 9, 'varie', label=part, size='s')
        arrow(ax, (42.5, yy + 4.5), (44.5, yy + 4.5), 'fixe', lw=0.8)
        box(ax, 45, yy, 40, 9, 'fixe', label='$' + g + '$', size='s')
    y -= n * step
save(fig, '60-237')
