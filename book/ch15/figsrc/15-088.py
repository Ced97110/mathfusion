import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
u = 6.4; x0 = 14; yt = 54
cols = [(r'$c = 4$', 4), (r'$d = 5$', 5)]
rows = [(r'$a = 3$', 3), (r'$b = 2$', 2)]
vals = {(0, 0): r'$ac = 12$', (1, 0): r'$bc = 8$', (0, 1): r'$ad = 15$', (1, 1): r'$bd = 10$'}
role = {(0, 0): 'resultat', (1, 1): 'resultat', (1, 0): 'limite', (0, 1): 'limite'}
cx = x0
for j, (lab, n) in enumerate(cols):
    ry = yt
    for i, (rl, m) in enumerate(rows):
        ry2 = ry - m * u
        ax.add_patch(Rectangle((cx, ry2), n * u, m * u, ec=COL[role[(i, j)]], fc=FILL[role[(i, j)]], lw=0.8, zorder=2,
                               ls='-' if role[(i, j)] == 'resultat' else '--'))
        text(ax, cx + n * u / 2, ry2 + m * u / 2, vals[(i, j)], role[(i, j)], 's')
        ry = ry2
    text(ax, cx + n * u / 2, yt + 4, lab, 'autre', 's')
    cx += n * u
ry = yt
for rl, m in rows:
    text(ax, 7, ry - m * u / 2, rl, 'sujet', 's')
    ry -= m * u
text(ax, 44, 14, r'$12 + 8 + 15 + 10 = 45$ : 4 produits', 'resultat', 's')
text(ax, 44, 6, r'$12 + 10 = 22$ : 2 produits, faux', 'limite', 's')
save(fig, '15-088')
