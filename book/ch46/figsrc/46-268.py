import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cx, cy, R = 24, 34, 20
def P(k): a = math.radians(90 - 360 * k / 12); return (cx + R * math.cos(a), cy + R * math.sin(a))
def loop(ax, x, y, role, r=3.0):
    c = (x, y + 1.5)
    ts = [math.radians(-60 + 300 * i / 30) for i in range(31)]
    pts = [(c[0] + r * math.cos(t), c[1] + r * math.sin(t)) for t in ts]
    line(ax, pts[:-1], role, lw=0.9)
    arrow(ax, pts[-2], pts[-1], role, lw=0.9)
for k in range(12):
    x, y = P(k); disc(ax, x, y, 3.2, 'sujet' if k == 0 else 'fixe', label=str(k))
x0, y0 = P(0)
loop(ax, x0, y0 + 3.2 - 1.5 + 0.5, 'varie')
text(ax, 66, 50, '⟨0⟩ = ⟨∅⟩ = {0}', 'sujet', 'm')
text(ax, 66, 36, 'multiples de 0 :', 'varie', 's')
text(ax, 66, 30, '0, 0, 0, …', 'varie', 'm')
save(fig, '46-268')
