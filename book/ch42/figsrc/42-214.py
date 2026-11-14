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
fig, ax = canvas(80)
xl, xr = 22, 66
y = [64, 53, 42]
els(ax, xl, y, [r'$s_1$', r'$s_2$', r'$s_3$'], 'sujet'); els(ax, xr, y, [r'$t_1$', r'$t_2$', r'$t_3$'], 'autre')
setbox(ax, xl, y, 'sujet', r'$S$'); setbox(ax, xr, y, 'autre', r'$T$')
for v in y: link(ax, xl, v, xr, v)
text(ax, 44, 28, r'injective : $m \leq n$', 'sujet', 's')
text(ax, 44, 21, r'surjective : $m \geq n$', 'autre', 's')
box(ax, 24, 4, 40, 10, 'resultat', label=r'$m = n = 3$')
arrow(ax, (44, 18), (44, 14.8), 'resultat')
save(fig, '42-214')
