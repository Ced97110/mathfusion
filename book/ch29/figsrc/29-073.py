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
fig, ax = canvas(52)
R = 14; a1 = math.degrees(1)
cl, cr, cy = 20, 62, 22
sector(ax, cl, cy, R, 0, a1, 'sujet'); arcline(ax, cl, cy, R, 0, a1)
x, y = P(cl, cy, R + 3.5, a1 / 2); text(ax, x, y, r'$r$', 'varie', 's')
for i in range(3):
    sector(ax, cr, cy, R, a1 * i, a1 * (i + 1), 'sujet'); arcline(ax, cr, cy, R, a1 * i, a1 * (i + 1))
    x, y = P(cr, cy, R + 3.5, a1 * (i + .5)); text(ax, x, y, r'$r$', 'varie', 's')
ray(ax, cr, cy, R, 0, 'sujet')
text(ax, cl, 14, '1 radian : arc = r', 'sujet', 's'); text(ax, cr, 14, '3 radians : arc = 3 r', 'sujet', 's')
text(ax, cr, 7, r'$r=2$ cm : $3\times2=6$ cm', 'resultat', 's')
save(fig, '29-073')
