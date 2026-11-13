import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
X = lambda x: 8 + (x + 2) * 10.5
Y = lambda v: 30 + 5 * v
a = math.atan(4.8)
for k in (-1, 0, 1, 2):
    xs = [k * math.pi - a + i * 2 * a / 60 for i in range(61)]
    xs = [x for x in xs if -2 <= x <= 5.4]
    if len(xs) > 1: line(ax, [(X(x), Y(math.tan(x))) for x in xs], 'varie', lw=1.2)
line(ax, [(X(-2), 30), (X(5.4), 30)], 'fixe', lw=0.6)
for x, lab in ((-math.pi / 2, '−π/2'), (math.pi / 2, 'π/2'), (3 * math.pi / 2, '3π/2')):
    line(ax, [(X(x), 5), (X(x), 56)], 'sujet', dash=True); text(ax, X(x), 2.5, lab, 'sujet', 's')
text(ax, 44, 65, 'asymptotes : x = π/2 + kπ', 'sujet', 'm')
text(ax, 44, 60, 'là où cos x = 0', 'fixe', 's')
save(fig, '30-052')
