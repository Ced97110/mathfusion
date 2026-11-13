import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
def curves(cx, cy, k, closed, role):
    ts = [i / 200 * 2 * math.pi for i in range(201)]
    if closed:
        line(ax, [(cx + k * 2 * math.cos(t), cy + k * 2 / math.sqrt(3) * math.sin(t)) for t in ts], role, lw=1.2)
    else:
        ys = [-2.4 + 4.8 * i / 100 for i in range(101)]
        for s in (-1, 1):
            line(ax, [(cx + s * k * math.sqrt(4 + 3 * y * y), cy + k * y) for y in ys], role, lw=1.2)
for cx in (22, 66):
    arrow(ax, (cx - 18, 36), (cx + 18, 36), 'fixe', lw=0.7)
    line(ax, [(cx, 22), (cx, 50)], 'fixe', lw=0.7)
curves(22, 36, 5.5, True, 'autre')
curves(66, 36, 3.4, False, 'sujet')
text(ax, 22, 70, r'$X^2 + 3Y^2 = 4$', 'autre', 'm')
text(ax, 66, 70, r'$X^2 - 3Y^2 = 4$', 'sujet', 'm')
text(ax, 22, 8, 'deux signes +\nfermée', 'autre', 's')
text(ax, 66, 8, 'un + et un −\nouverte', 'sujet', 's')
text(ax, 66, 63, r'$X^2 = 4 + 3Y^2 > 0$', 'resultat', 's')
save(fig, '71-162')
