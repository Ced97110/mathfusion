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
fig, ax = canvas(66)
xl, xr = 22, 66
yl = [46, 35, 24]; yr = [40.5, 29.5]
els(ax, xl, yl, [r'$s_1$', r'$s_2$', r'$s_3$'], 'sujet'); els(ax, xr, yr, [r'$t_1$', r'$t_2$'], 'autre')
setbox(ax, xl, yl, 'sujet', r'$S$'); setbox(ax, xr, yr, 'autre', r'$T$')
link(ax, xl, yl[0], xr, yr[0]); link(ax, xl, yl[1], xr, yr[1], 'limite'); link(ax, xl, yl[2], xr, yr[1], 'limite')
text(ax, 22, 12, r'$m = 3$', 'sujet', 'm'); text(ax, 66, 12, r'$n = 2$', 'autre', 'm')
text(ax, 44, 4, 'deux départs, même arrivée', 'limite', 's')
text(ax, 44, 57, r'injection $\Rightarrow m \leq n$', 'resultat', 's')
save(fig, '42-212')
