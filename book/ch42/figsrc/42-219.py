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
fig, ax = canvas(64)
xs = [20, 44, 68]
for x, l, r in zip(xs, [r'$g$', r'$\circ$', r'$f$'], ['sujet', 'varie', 'autre']):
    box(ax, x - 9, 42, 18, 14, r, label=l, size='l')
notes = ['agit en second', '« rond »', 'agit en premier']
for x, n, r in zip(xs, notes, ['sujet', 'varie', 'autre']):
    arrow(ax, (x, 41), (x, 31), r); text(ax, x, 26, n, r, 's')
box(ax, 6, 3, 76, 10, 'resultat', label=r'$g \circ f$ = d’abord $f$, puis $g$', size='s')
text(ax, 44, 62, 'deux noms et un signe', 'fixe', 's')
save(fig, '42-219')
