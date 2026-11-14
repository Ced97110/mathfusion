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
text(ax, 10, 45, 'degrés', 'fixe', 's'); text(ax, 10, 19, 'radians', 'fixe', 's')
box(ax, 22, 40, 10, 10, 'fixe', r'$r$', 'm'); text(ax, 35, 45, '×', 'encre', 'm')
box(ax, 38, 40, 10, 10, 'sujet', r'$d$', 'm'); text(ax, 51, 45, '×', 'encre', 'm')
box(ax, 54, 40, 18, 10, 'varie', r'$\pi/180$', 'm'); text(ax, 80, 45, r'$=s$', 'encre', 'm')
box(ax, 22, 14, 10, 10, 'fixe', r'$r$', 'm'); text(ax, 35, 19, '×', 'encre', 'm')
box(ax, 38, 14, 34, 10, 'sujet', r'$d\times\pi/180$', 'm', dash=True); text(ax, 80, 19, r'$=s$', 'encre', 'm')
text(ax, 55, 28, r'$\theta$', 'sujet', 'm')
arrow(ax, (63, 40), (63, 31), 'varie')
text(ax, 44, 6, 'le facteur est dans θ', 'resultat', 's')
save(fig, '29-077')
