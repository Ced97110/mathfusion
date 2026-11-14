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
fig, ax = canvas(70)
u = 7; cx, cy, R = 22, 40, 3 * u; th = math.degrees(2)
sector(ax, cx, cy, R, 0, th, 'sujet'); ray(ax, cx, cy, R, 0, 'sujet'); arcline(ax, cx, cy, R, 0, th, 'varie', 2.4)
text(ax, cx + R / 2, cy - 3, r'$r=3$ cm', 'sujet', 's')
x, y = P(cx, cy, 9, th / 2); text(ax, x, y, r'$\theta=2$', 'sujet', 's')
x, y = P(cx, cy, R + 4, th / 2); text(ax, x, y, r'$s$', 'varie', 'm')
text(ax, 22, 21, 'arc déroulé', 'varie', 's', ha='left')
for i in range(2): box(ax, 22 + R * i, 10, R, 7, 'sujet', r'$r$', 's')
brace(ax, 22, 22 + 2 * R, 10, 'varie', r'$s=3\times2=6$ cm', down=True)
save(fig, '29-071')
