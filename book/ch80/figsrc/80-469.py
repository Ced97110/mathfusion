import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cut(p, q, r):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    return [(p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r)]
fig, ax = canvas(64)
def diamond(cx, labels, r, size):
    pts = [(cx, 12), (cx - 11, 29), (cx + 11, 29), (cx, 46)]
    for i, j in ((0, 1), (0, 2), (1, 3), (2, 3)): line(ax, cut(pts[i], pts[j], r), 'fixe')
    for p, l, role in zip(pts, labels, ['fixe', 'sujet', 'varie', 'resultat']): disc(ax, p[0], p[1], r, role, label=l, size=size)
diamond(18, [r'$O$', r'$a$', r"$a'$", r'$I$'], 4.2, 'm')
diamond(70, [r'$\emptyset$', r'$\{1\}$', r'$\{2\}$', r'$\{1,2\}$'], 5.6, 's')
text(ax, 18, 58, 'circuit à une lettre', 'encre', 's'); text(ax, 70, 58, r'parties de $\{1,2\}$', 'encre', 's')
text(ax, 44, 29, 'même', 'varie', 's'); text(ax, 44, 25, 'structure', 'varie', 's')
text(ax, 44, 4, 'même couleur : même rôle', 'fixe', 's')
save(fig, '80-469')
