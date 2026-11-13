import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **kw):
    return _box(ax, x, y, w, h, role, label=label, size=size, **kw)
def P(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
def arcpts(cx, cy, r, a0, a1, n=48):
    return [P(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]
def sector(ax, cx, cy, r, a0, a1, role='sujet'):
    poly(ax, [(cx, cy)] + arcpts(cx, cy, r, a0, a1), role)
def arcline(ax, cx, cy, r, a0, a1, role='varie', lw=2.0):
    line(ax, arcpts(cx, cy, r, a0, a1), role, lw=lw)
def ray(ax, cx, cy, r, a, role='fixe'):
    line(ax, [(cx, cy), P(cx, cy, r, a)], role)
fig, ax = canvas(62)
text(ax, 30, 58, 'rayon', 'sujet', 's'); text(ax, 58, 58, 'angle (radians)', 'varie', 's')
box(ax, 22, 40, 16, 13, 'sujet', r'$r$', 'l'); box(ax, 38, 40, 16, 13, 'varie', r'$\theta$', 'l')
arrow(ax, (38, 38), (38, 31), 'fixe')
text(ax, 38, 26, r'$r\times\theta$', 'encre', 'l')
text(ax, 62, 35, 'côte à côte = fois', 'fixe', 's')
text(ax, 38, 12, r'$r=3,\ \theta=2$ : $3\times2=6$', 'resultat', 'm')
save(fig, '29-072')
