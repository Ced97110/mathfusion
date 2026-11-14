import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
X = lambda x: 8 + (x + 2) * 10.5
Y = lambda v: 32 + 5 * v
a = math.atan(4.8)
for k, role in ((0, 'sujet'), (1, 'fixe')):
    line(ax, [(X(k * math.pi - a + i * 2 * a / 60), Y(math.tan(k * math.pi - a + i * 2 * a / 60))) for i in range(61)], role, lw=1.6 if k == 0 else 1.1)
line(ax, [(X(-2), 32), (X(5.4), 32)], 'fixe', lw=0.6)
for x, lab in ((-math.pi / 2, '−π/2'), (math.pi / 2, 'π/2'), (3 * math.pi / 2, '3π/2')):
    line(ax, [(X(x), 12), (X(x), 58)], 'fixe', dash=True); text(ax, X(x), 3.5, lab, 'fixe', 's')
arrow(ax, (X(-math.pi / 2), 62), (X(math.pi / 2), 62), 'varie', both=True); text(ax, X(0), 65, 'largeur π', 'varie', 's')
text(ax, X(0) - 8, 22, 'une branche', 'sujet', 's')
text(ax, X(-math.pi / 2) + 1.5, 52, 'asymptote', 'fixe', 's', ha='left')
save(fig, '30-058')
