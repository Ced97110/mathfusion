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
f = numberline(ax, 12, 70, 28, 0, 3, 1, labels=False, arrow_right=False)
line(ax, [(f(0), 28), (f(1), 28)], 'varie', lw=2.6)
for v, a, b in [(0, '0', '0°'), (1, r'$\pi/3$', '60°'), (2, r'$2\pi/3$', '120°'), (3, r'$\pi$', '180°')]:
    text(ax, f(v), 34, a, 'varie' if v == 1 else 'fixe', 's')
    text(ax, f(v), 22, b, 'varie' if v == 1 else 'fixe', 's')
brace(ax, f(0), f(1), 38, 'varie', 'un tiers', down=False)
text(ax, 44, 9, r'$60°=\pi/3$', 'sujet', 'l')
text(ax, 44, 15.5, 'trois tiers = un demi-tour', 'fixe', 's')
save(fig, '29-067')
