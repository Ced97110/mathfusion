import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
for y0, M, role, cap, bad in [(36, [[1, 0, 1], [0, 1, 1]], 'resultat', r'différentes : $d \geq 3$', False),
                              (8, [[1, 1, 1], [0, 0, 1]], 'limite', r'égales : $d \leq 2$', True)]:
    for r in range(2):
        for c in range(3):
            box(ax, 8 + 9 * c, y0 + 9 - 9 * r, 9, 8, 'limite' if (bad and c < 2) else 'sujet', label=str(M[r][c]))
    box(ax, 7, y0 - 1, 29, 19, role, fill=False, dash=True)
    text(ax, 40, y0 + 9, cap, role, 's', ha='left')
save(fig, '68-117')
