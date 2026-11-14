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
fig, ax = canvas(60)
cx, cy, R = 24, 30, 20
for i in range(4):
    sector(ax, cx, cy, R, 90 * i, 90 * (i + 1), 'varie' if i == 0 else 'fixe')
    x, y = P(cx, cy, 11, 90 * i + 45); text(ax, x, y, '7,07 cm²' if i == 0 else '7,07', 'varie' if i == 0 else 'fixe', 's')
text(ax, 68, 50, r'$r=3$ cm', 'fixe', 's')
text(ax, 68, 42, 'disque : 28,27 cm²', 'sujet', 's')
text(ax, 68, 28, '¼ de tour : ¼ de l’aire', 'resultat', 's')
text(ax, 68, 18, r'$4\times7{,}07\approx28{,}27$', 'fixe', 's')
save(fig, '29-079')
