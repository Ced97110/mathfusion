import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx, cy, hw, hh = 40, 32, 36, 24
poly(ax, [(cx - hw, cy - hh), (cx + hw, cy - hh), (cx + hw, cy + hh), (cx - hw, cy + hh)], 'fixe')
def ends(deg):
    t = math.radians(deg); dx, dy = math.cos(t), math.sin(t)
    s = min(hw / abs(dx) if abs(dx) > 1e-9 else 1e9, hh / abs(dy) if abs(dy) > 1e-9 else 1e9)
    return (cx - s * dx, cy - s * dy), (cx + s * dx, cy + s * dy)
for d in (10, 22, 52, 70, 100, 135, 150, 165):
    a, b = ends(d); line(ax, [a, b], 'fixe', 0.7)
a, b = ends(118); line(ax, [a, b], 'varie', 1.8)
text(ax, b[0] + 3, b[1] - 3.5, r'$\ell$', 'varie', 'l')
named = [('AB', 0, 'sujet'), ('AD', 90, 'sujet'), ('AC', 36.87, 'sujet')]
for n, d, r in named:
    a, b = ends(d); line(ax, [a, b], r, 1.3)
text(ax, cx + hw - 4, cy + 3, 'AB', 'sujet', 's'); text(ax, cx + 3, cy + hh - 3, 'AD', 'sujet', 's')
text(ax, cx + 28, cy + 21.5, 'AC', 'sujet', 's')
disc(ax, cx, cy, 1.2, 'encre'); text(ax, cx - 3, cy - 3, 'A', 'encre')
text(ax, 20, 4, 'plan', 'fixe', 's')
text(ax, 62, 4, r'$\ell$ : n’importe laquelle', 'varie', 's')
save(fig, '27-046')
