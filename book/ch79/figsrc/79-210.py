import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def nb(ax, cx, cy, w, h, role, label, size="s", fill=True):
    box(ax, cx - w / 2, cy - h / 2, w, h, role, label=label, size=size, fill=fill)
def ed(ax, p, q, role="fixe", t=5.0, lw=0.9, head=False):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    a = (p[0] + ux * t, p[1] + uy * t); b = (q[0] - ux * t, q[1] - uy * t)
    if head: arrow(ax, a, b, role, lw=lw)
    else: line(ax, [a, b], role, lw=lw)

fig, ax = canvas(84)
text(ax, 18, 79, 'sous-groupes', 'sujet', 'm', weight='bold')
text(ax, 65, 79, 'corps fixes', 'autre', 'm', weight='bold')
yT, yM, yB = 64, 46, 28
nb(ax, 18, yT, 14, 8, 'sujet', r'$G$')
for x, l in [(7, r'$H_1$'), (18, r'$H_2$'), (29, r'$H_3$')]:
    nb(ax, x, yM, 9, 8, 'sujet', l); ed(ax, (x, yM), (18, yT), 'fixe', 4.5); ed(ax, (x, yM), (18, yB), 'fixe', 4.5)
nb(ax, 18, yB, 14, 8, 'sujet', r'$\{e\}$')
nb(ax, 65, yT, 28, 8, 'autre', r'$\mathbb{Q}(\sqrt{2},\sqrt{3})$')
for x, l in [(50, r'$\mathbb{Q}(\sqrt{2})$'), (65, r'$\mathbb{Q}(\sqrt{3})$'), (80, r'$\mathbb{Q}(\sqrt{6})$')]:
    nb(ax, x, yM, 14, 8, 'autre', l); ed(ax, (x, yM), (65, yT), 'fixe', 4.5); ed(ax, (x, yM), (65, yB), 'fixe', 4.5)
nb(ax, 65, yB, 14, 8, 'autre', r'$\mathbb{Q}$')
arrow(ax, (26, yT - 3), (58, yB + 3), 'resultat', lw=1.1)
arrow(ax, (26, yB + 3), (58, yT - 3), 'varie', lw=1.1)
text(ax, 44, 16, r'sup de $H_1$, $H_2$ : $G$ $\leftrightarrow$ $\mathbb{Q}$', 'resultat', 's')
text(ax, 44, 9, r'inf $\{e\}$ $\leftrightarrow$ plus petit corps', 'varie', 's')
text(ax, 44, 2.8, 'sup devient intersection', 'resultat', 's')
save(fig, '79-210')
