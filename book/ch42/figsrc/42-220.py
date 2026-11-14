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
fig, ax = canvas(86)
text(ax, 44, 80, r'$g \circ f$ : $f$ d’abord, puis $g$', 'encre', 'm')
arrow(ax, (58, 72), (30, 72), 'varie', curve=-0.35)
text(ax, 44, 64, 'lire de droite à gauche', 'varie', 's')
def row(y, a, b, c, d, e, r, name):
    box(ax, 3, y - 5, 12, 10, 'sujet', label=r'$4$')
    box(ax, 38, y - 5, 12, 10, 'fixe', label=b)
    box(ax, 73, y - 5, 12, 10, r, label=c)
    arrow(ax, (16, y), (37, y), 'varie'); arrow(ax, (51, y), (72, y), 'varie')
    text(ax, 26.5, y + 5.5, a, 'varie', 's'); text(ax, 61.5, y + 5.5, d, 'varie', 's')
    text(ax, 44, y + 13, name, r, 's')
row(46, r'$f$ : $+2$', r'$6$', r'$18$', r'$g$ : $\times 3$', None, 'resultat', 'f puis g : 18')
row(14, r'$g$ : $\times 3$', r'$12$', r'$14$', r'$f$ : $+2$', None, 'limite', 'g puis f : 14')
save(fig, '42-220')
