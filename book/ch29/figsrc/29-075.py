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
fig, ax = canvas(50)
cx, cy, R = 20, 12, 18; a1 = math.degrees(1)
sector(ax, cx, cy, R, 0, 2 * a1, 'sujet'); ray(ax, cx, cy, R, a1, 'sujet')
arcline(ax, cx, cy, R, 0, 2 * a1)
for i, y in enumerate((17.7, 24)):
    x2, y2 = P(cx, cy, 12, a1 * (i + .5)); text(ax, x2, y2, '1 rad', 'sujet', 's')
text(ax, 44, 44, '1 radian : arc r', 'varie', 's', ha='left')
box(ax, 44, 36, R, 5, 'varie', r'$r$', 's')
text(ax, 44, 30, '2 radians : arc 2 r', 'varie', 's', ha='left')
for i in range(2): box(ax, 44 + R * i, 22, R, 5, 'varie', r'$r$', 's')
text(ax, 62, 12, 'angle ×2 : arc ×2', 'resultat', 's')
save(fig, '29-075')
