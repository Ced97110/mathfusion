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
fig, ax = canvas(54)
cx, cy, R = 40, 10, 30
sector(ax, cx, cy, R, 0, 180, 'fixe')
sector(ax, cx, cy, R, 0, 30, 'sujet')
for a in range(30, 180, 30): ray(ax, cx, cy, R, a)
arcline(ax, cx, cy, R, 0, 30)
x, y = P(cx, cy, 19, 15); text(ax, x, y, '30°', 'sujet', 's')
x, y = P(cx, cy, 37, 15); text(ax, x, y, r'$\pi/6$', 'varie', 'm')
text(ax, cx, 4.5, r'180° $=\pi$ : 6 parts de 30°', 'fixe', 's')
text(ax, cx, 49, 'un sixième du demi-tour', 'sujet', 's')
save(fig, '29-065')
