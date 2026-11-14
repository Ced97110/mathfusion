import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def tri(cx, cy, r, role):
    pts = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))) for a in (90, -30, -150)]
    for i in range(3):
        p, q = pts[i], pts[(i + 1) % 3]
        dx, dy = q[0] - p[0], q[1] - p[1]; L = math.hypot(dx, dy); k = 3.4 / L
        arrow(ax, (p[0] + dx * k, p[1] + dy * k), (q[0] - dx * k, q[1] - dy * k), role)
    for (x, y) in pts: disc(ax, x, y, 2.4, role)
tri(14, 58, 9, 'sujet'); tri(40, 58, 9, 'varie')
disc(ax, 14, 28, 2.4, 'resultat'); disc(ax, 26, 28, 2.4, 'resultat')
text(ax, 27, 45, '2 cycles de longueur 3', 'encre', 's')
text(ax, 20, 20, '2 points fixes', 'resultat', 's')
text(ax, 27, 74, r'ordre de $\varphi$ = 3', 'encre', 's')
for i, s in enumerate(('1', r'$\alpha$', r'$\alpha^2$')): box(ax, 60 + i * 8.6, 54, 8.4, 9, 'autre', label=s, size='s')
brace(ax, 60, 85.6, 54, 'autre', label='base : 3 éléments', down=True)
box(ax, 14, 2, 60, 10, 'resultat', label=r'$3=[\mathbb{F}_8:\mathbb{F}_2]$')
save(fig, '67-097')
