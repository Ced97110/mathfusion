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
cx, cy, R = 40, 12, 28
sector(ax, cx, cy, R, 0, 90, 'sujet'); sector(ax, cx, cy, R, 90, 180, 'fixe')
arcline(ax, cx, cy, R, 0, 90)
line(ax, [(cx + 3, cy), (cx + 3, cy + 3), (cx, cy + 3)], 'sujet', lw=0.8)
text(ax, cx + 11, cy + 14, '90°', 'sujet', 's'); text(ax, cx + 11, cy + 8.5, r'$\pi/2$', 'sujet', 's')
text(ax, cx - 11, cy + 14, '90°', 'fixe', 's'); text(ax, cx - 11, cy + 8.5, r'$\pi/2$', 'fixe', 's')
text(ax, 77, 30, 'arc ≈ 1,571', 'varie', 's')
text(ax, cx, 6, r'180° $=\pi$ : deux angles droits', 'fixe', 's')
save(fig, '29-068')
