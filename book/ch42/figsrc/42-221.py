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
fig, ax = canvas(72)
def row(y, a, b, c, la, lb, r, name):
    box(ax, 3, y - 5, 12, 10, 'sujet', label=a, size='m')
    box(ax, 38, y - 5, 12, 10, 'fixe', label=b, size='m')
    box(ax, 73, y - 5, 12, 10, r, label=c, size='m')
    arrow(ax, (16, y), (37, y), 'varie'); arrow(ax, (51, y), (72, y), 'varie')
    text(ax, 26.5, y + 5.5, la, 'varie', 's'); text(ax, 61.5, y + 5.5, lb, 'varie', 's')
    text(ax, 44, y + 13.5, name, 'encre', 'm')
row(54, r'$1$', r'$7$', r'$49$', r'$g$ : $2x+5$', r'$f$ : $x^2$', 'resultat', r'$f \circ g$')
row(22, r'$1$', r'$1$', r'$7$', r'$f$ : $x^2$', r'$g$ : $2x+5$', 'limite', r'$g \circ f$')
text(ax, 44, 4, r'$49 \neq 7$ : l’ordre change le résultat', 'limite', 's')
save(fig, '42-221')
