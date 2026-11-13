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
fig, ax = canvas(66)
text(ax, 24, 60, 'exact', 'resultat', 's'); text(ax, 64, 60, 'arrondi', 'varie', 's')
box(ax, 11, 42, 26, 9, 'resultat', r'$\pi/3$', 'm'); box(ax, 51, 42, 26, 9, 'varie', '1,047', 'm')
arrow(ax, (24, 42), (24, 29), 'fixe'); arrow(ax, (64, 42), (64, 29), 'fixe')
text(ax, 31, 35.5, r'$\times3$', 'fixe', 's'); text(ax, 71, 35.5, r'$\times3$', 'fixe', 's')
box(ax, 11, 19, 26, 9, 'resultat', r'$\pi$', 'm'); box(ax, 51, 19, 26, 9, 'limite', '3,141', 'm')
text(ax, 24, 11, 'exactement π', 'resultat', 's'); text(ax, 64, 11, r'$\neq\pi$', 'limite', 'm')
save(fig, '29-070')
