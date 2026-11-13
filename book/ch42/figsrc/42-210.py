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
fig, ax = canvas(76)
xl, xr = 22, 66
yl = [56, 45, 34, 23]; yr = [56, 40, 23]
els(ax, xl, yl, [r'$1/2$', r'$1/3$', r'$0/1$', r'$5/1$'], 'sujet')
els(ax, xr, yr, [r'$1$', r'$0$', r'$5$'], 'resultat')
setbox(ax, xl, yl, 'sujet', r'$\mathbb{Q}$'); setbox(ax, xr, yr, 'autre', r'$\mathbb{Z}$')
link(ax, xl, yl[0], xr, yr[0], 'limite'); link(ax, xl, yl[1], xr, yr[0], 'limite')
link(ax, xl, yl[2], xr, yr[1]); link(ax, xl, yl[3], xr, yr[2])
text(ax, 44, 67, r'$g: p/q \mapsto p$', 'varie', 'm')
text(ax, 44, 61, 'fraction irréductible', 'fixe', 's')
text(ax, 22, 9, 'non injective\n1/2 et 1/3 $\\to$ 1', 'limite', 's')
text(ax, 66, 9, 'surjective\nchaque entier reçu', 'resultat', 's')
save(fig, '42-210')
