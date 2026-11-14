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
rows = [('0°', '0'), ('30°', r'$\pi/6$'), ('45°', r'$\pi/4$'), ('60°', r'$\pi/3$'),
        ('90°', r'$\pi/2$'), ('180°', r'$\pi$'), ('270°', r'$3\pi/2$'), ('360°', r'$2\pi$')]
text(ax, 44, 59, 'degrés → radians', 'encre', 's')
for i, (d, r) in enumerate(rows):
    col, k = divmod(i, 4)
    role = 'sujet' if 1 <= i <= 4 else 'fixe'
    box(ax, 4 + 42 * col, 40 - 12 * k, 38, 9, role, d + ' → ' + r, 'm')
save(fig, '29-069')
