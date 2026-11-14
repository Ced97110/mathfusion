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
fig, ax = canvas(48)
cx, cy, R = 28, 8, 26
for i in range(4):
    sector(ax, cx, cy, R, 45 * i, 45 * (i + 1), 'sujet')
    x, y = P(cx, cy, 12, 45 * i + 22.5); text(ax, x, y, '45°', 'sujet', 's')
    x, y = P(cx, cy, 21, 45 * i + 22.5); text(ax, x, y, r'$\pi/4$', 'varie', 's')
arcline(ax, cx, cy, R, 0, 180, 'fixe', 1.0)
text(ax, 72, 30, r'$4\times 45°=180°$', 'encre', 's')
text(ax, 72, 22, r'$4\times\pi/4=\pi$', 'resultat', 's')
text(ax, 72, 14, 'quatre angles égaux', 'fixe', 's')
save(fig, '29-066')
