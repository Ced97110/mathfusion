import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
R=3.6
def els(ax, x, ys, labels, role, dashed=False):
    for y, l in zip(ys, labels):
        disc(ax, x, y, R, role, label=l)
def setbox(ax, x, ys, role, name=None, w=14, pad=5):
    box(ax, x - w/2, min(ys) - pad, w, max(ys) - min(ys) + 2*pad, role, fill=False)
    if name: text(ax, x, max(ys) + pad + 2.6, name, role, 'l')
def link(ax, xa, ya, xb, yb, role='varie', curve=0.0):
    arrow(ax, (xa + R + 0.4, ya), (xb - R - 0.4, yb), role, curve=curve)
fig, ax = canvas(62)
xl, xr = 22, 66
yl = [46, 35, 24]; yr = [46, 35, 24, 13]
els(ax, xl, yl, [r'$-1$', r'$0$', r'$3$'], 'sujet')
els(ax, xr, yr[:3], [r'$-1/1$', r'$0/1$', r'$3/1$'], 'resultat')
disc(ax, xr, yr[3], R, 'limite', label=r'$1/2$')
setbox(ax, xl, yl, 'sujet', r'$\mathbb{Z}$'); setbox(ax, xr, yr, 'autre', r'$\mathbb{Q}$', w=18)
for a, b in zip(yl, yr): link(ax, xl + 2, a, xr - 2, b)
text(ax, 44, 54, r'$f: n \mapsto n/1$', 'varie', 'm')
text(ax, 22, 4, 'arrivées toutes différentes', 'resultat', 's')
text(ax, 66, 4, 'aucune flèche', 'limite', 's')
save(fig, '42-209')
