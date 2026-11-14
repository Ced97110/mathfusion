import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
def sector(c, r, a0, a1, role):
    pts = [c] + [(c[0] + r*math.cos(math.radians(a0 + (a1 - a0)*i/30)), c[1] + r*math.sin(math.radians(a0 + (a1 - a0)*i/30))) for i in range(31)]
    poly(ax, pts, role)
def ray(c, a, r=34, role='fixe'):
    line(ax, [c, (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))], role)
def at(c, a, r): return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
c1 = (4, 10); c2 = (50, 10)
sector(c1, 32, 0, 45, 'sujet'); sector(c1, 32, 45, 75, 'varie')
for a in (0, 45, 75): ray(c1, a)
x, y = at(c1, 22, 20); text(ax, x, y, 'A = 45°', 'sujet', 's')
x, y = at(c1, 60, 22); text(ax, x, y, 'B = 30°', 'varie', 's')
text(ax, 20, 4, 'A + B = 75°', 'resultat', 'm')
sector(c2, 32, 0, 30, 'varie'); sector(c2, 32, 30, 45, 'resultat')
for a in (0, 30, 45): ray(c2, a)
x, y = at(c2, 12, 22); text(ax, x, y, 'B = 30°', 'varie', 's')
x, y = at(c2, 45, 38); text(ax, x, y, 'A = 45°', 'sujet', 's')
text(ax, 66, 4, 'A − B = 15°', 'resultat', 'm')
save(fig, '34-009')
