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
for i in range(4):
    r = 'varie' if i == 0 else 'fixe'
    box(ax, 14 + 15 * i, 36, 15, 8, r, '45°', 's')
    box(ax, 14 + 15 * i, 12, 15, 8, r, r'$\pi/4$', 's')
brace(ax, 14, 74, 46, 'fixe', '180° : un demi-tour', down=False)
brace(ax, 14, 74, 12, 'fixe', r'$\pi$ : un demi-tour', down=True)
arrow(ax, (21.5, 36), (21.5, 20), 'varie')
text(ax, 50, 28, 'même fraction : un quart', 'varie', 's')
save(fig, '29-064')
