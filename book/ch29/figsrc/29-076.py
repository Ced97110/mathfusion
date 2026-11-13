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
fig, ax = canvas(64)
cx, cy, R = 22, 38, 18
disc(ax, cx, cy, R, 'fixe', fill=False); sector(ax, cx, cy, R, 0, 12, 'varie'); ray(ax, cx, cy, R, 0, 'fixe')
text(ax, cx + 9, cy - 3.5, r'$r=500$ m', 'fixe', 's')
text(ax, cx + R + 2, cy + 4.5, r'$d=12°$', 'varie', 's', ha='left')
text(ax, cx, 14, 'un tour : 360°', 'fixe', 's')
box(ax, 58, 48, 28, 9, 'fixe', r'tour : $2\pi\times500$', 's')
box(ax, 58, 32, 28, 9, 'varie', 'part : 12/360', 's')
box(ax, 58, 16, 28, 9, 'resultat', r'$s\approx104{,}7$ m', 's')
arrow(ax, (72, 48), (72, 41), 'fixe'); arrow(ax, (72, 32), (72, 25), 'fixe')
save(fig, '29-076')
