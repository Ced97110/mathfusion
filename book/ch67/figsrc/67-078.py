import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# non-zero elements of the field with 5 elements, in the order of the powers of 2 : 2, 4, 3, 1
cx, cy, R = 27, 36, 20
vals = [2, 4, 3, 1]
angs = [90, 0, -90, 180]
pos = lambda a, r=R: (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
for k in range(4):
    a0, a1 = angs[k] - 22, angs[(k + 1) % 4] + 22
    arrow(ax, pos(a0), pos(a1), 'fixe', curve=-0.15)
for k, v in enumerate(vals):
    x, y = pos(angs[k])
    disc(ax, x, y, 5.2, 'varie' if v in (1, 4) else 'sujet', label=str(v))
text(ax, cx, cy, 'puissances\nde 2', 'sujet', 's')
disc(ax, 58, 56, 2.6, 'varie')
text(ax, 62, 56, r'$x^2 = 1$', 'varie', 's', ha='left')
text(ax, 62, 49, 'solutions : 1 et 4', 'varie', 's', ha='left')
disc(ax, 58, 34, 2.6, 'sujet')
text(ax, 62, 34, 'autres', 'sujet', 's', ha='left')
text(ax, 58, 14, 'au plus 2 solutions', 'fixe', 's', ha='left')
save(fig, '67-078')
