import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def P(cx, cy, r, a):
    return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))

def arc(ax, cx, cy, r, a0, a1, role, lw=1.0):
    line(ax, [P(cx, cy, r, a0 + (a1 - a0) * i / 60) for i in range(61)], role, lw)

def axes(ax, cx, cy, R):
    line(ax, [(cx - R - 3, cy), (cx + R + 3, cy)], 'fixe', 0.5)
    line(ax, [(cx, cy - R - 3), (cx, cy + R + 3)], 'fixe', 0.5)

fig, ax = canvas(62)
fa = lambda v: 8 + v / 1440 * 64
fb = lambda v: 8 + v / 288 * 64
numberline(ax, 8, 72, 48, 0, 1440, 360, labels=False, role='varie', arrow_right=False)
numberline(ax, 8, 72, 20, 0, 288, 72, labels=False, role='sujet', arrow_right=False)
text(ax, 44, 57, '5θ = 360° × m (m tours)', 'varie', 'm')
for k in range(5):
    text(ax, fa(360 * k), 44.6, f'{360 * k}°', 'varie', 's')
    text(ax, fb(72 * k), 16.6, f'{72 * k}°', 'sujet', 's')
    line(ax, [(fa(360 * k), 42), (fb(72 * k), 23)], 'fixe', 0.6, dash=True)
text(ax, 80, 33, '÷ 5', 'varie', 'm')
brace(ax, 8, 72, 12, 'resultat', label='θ : 5 solutions par tour', depth=1.6)
save(fig, '32-156')
