import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
R=2.6
def els(ax, x, ys, labels, role, dashed=False):
    for y, l in zip(ys, labels):
        disc(ax, x, y, R, role, label=l)
def setbox(ax, x, ys, role, name=None, w=14, pad=5):
    box(ax, x - w/2, min(ys) - pad, w, max(ys) - min(ys) + 2*pad, role, fill=False)
    if name: text(ax, x, max(ys) + pad + 2.6, name, role, 'l')
def link(ax, xa, ya, xb, yb, role='varie', curve=0.0):
    arrow(ax, (xa + R + 0.4, ya), (xb - R - 0.4, yb), role, curve=curve)
fig, ax = canvas(88)
# finis
text(ax, 44, 82, 'Ensembles finis', 'resultat', 'l')
els(ax, 18, [72, 62], [r'$s_1$', r'$s_2$'], 'sujet'); els(ax, 70, [74, 67, 60], [r'$t_1$', r'$t_2$', r'$t_3$'], 'autre')
link(ax, 18, 72, 70, 74, curve=0); link(ax, 18, 62, 70, 67)
text(ax, 44, 55, r'injection : $m \leq n$ : vrai', 'resultat', 's')
line(ax, [(4, 50), (84, 50)], 'fixe', dash=True)
text(ax, 44, 45, 'Ensembles infinis', 'limite', 'l')
box(ax, 8, 8, 26, 30, 'sujet', label=None); box(ax, 54, 8, 26, 30, 'autre', label=None)
text(ax, 21, 33, r'$\mathbb{Z}$', 'sujet', 'l'); text(ax, 67, 33, r'$\mathbb{Q}$', 'autre', 'l')
text(ax, 21, 21, r'$\ldots$', 'sujet', 'l'); text(ax, 67, 21, r'$\ldots$', 'autre', 'l')
arrow(ax, (35, 30), (53, 30), 'varie'); arrow(ax, (53, 15), (35, 15), 'varie')
text(ax, 44, 34, 'injective', 'varie', 's'); text(ax, 44, 11, 'surjective', 'varie', 's')
text(ax, 44, 22, 'plus grand ?', 'limite', 's')
save(fig, '42-211')
