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
cx, cy, R = 12, 34, 26
sector(ax, cx, cy, R, 0, 30, 'sujet'); ray(ax, cx, cy, R, 0, 'sujet'); arcline(ax, cx, cy, R, 0, 30)
text(ax, cx + 13, cy - 3.5, r'$r=3$ cm', 'sujet', 's')
x, y = P(cx, cy, 16, 15); text(ax, x, y, '30°', 'sujet', 's')
text(ax, 66, 58, 'avec θ = 30 : faux', 'limite', 's')
box(ax, 46, 44, 40, 10, 'limite', r'$3\times30=90$ cm', 'm')
text(ax, 66, 38, 'en radians : vrai', 'resultat', 's')
box(ax, 46, 24, 40, 10, 'resultat', r'$s\approx1{,}57$ cm', 'm')
text(ax, 44, 10, 'θ doit être en radians', 'encre', 's')
save(fig, '29-078')
