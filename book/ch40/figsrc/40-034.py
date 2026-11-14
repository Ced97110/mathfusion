import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# cardioïde r = 1 + cos θ : f(π) = 0 ; θ = 170° -> r ≈ 0,015 ; 175° -> r ≈ 0,004. Loupe ×1000.
fig, ax = canvas(74)
f = lambda t: 1 + math.cos(t)
# vue d'ensemble
o = (8, 44); u = 13
pts = [(o[0] + u * f(t) * math.cos(t), o[1] + u * f(t) * math.sin(t)) for t in [i * 2 * math.pi / 300 for i in range(301)]]
line(ax, pts, 'sujet', lw=1.2)
line(ax, [(o[0] - 5, o[1]), (o[0] + 30, o[1])], 'fixe')
disc(ax, o[0], o[1], 1.8, 'varie', fill=False, lw=1.0)
text(ax, o[0] + 13, o[1] - 18, r'$r = 1 + \cos\theta$', 'sujet', 's')
text(ax, o[0] + 3, o[1] + 22, 'pointe en O', 'varie', 's')
# loupe : échelle 1000 mm par unité, pôle en p
box(ax, 44, 4, 42, 62, 'fixe', fill=False, dash=True)
text(ax, 65, 69, 'loupe ×1000 autour de O', 'varie', 's')
p = (82, 35); S = 1000.0
def L(r, deg):
    return (p[0] + S * r * math.cos(math.radians(deg)), p[1] + S * r * math.sin(math.radians(deg)))
tt = [163 + i * 0.5 for i in range(0, 35)]
up = [L(f(math.radians(a)), a) for a in tt]
line(ax, up, 'sujet', lw=1.2)
line(ax, [(x, 2 * p[1] - y) for x, y in up], 'sujet', lw=1.2)
line(ax, [(46, p[1]), (84, p[1])], 'fixe')
for a, y0, lab in [(170, 56, r'170° : $r \approx$ 0,015'), (175, 17, r'175° : $r \approx$ 0,004')]:
    q = L(f(math.radians(a)), a)
    c, s = math.cos(math.radians(a)), math.sin(math.radians(a))
    line(ax, [p, (p[0] + 36 * c, p[1] + 36 * s)], 'fixe', dash=True)
    disc(ax, q[0], q[1], 0.9, 'varie')
    line(ax, [(q[0], q[1] + 1 if y0 > 35 else q[1] - 1), (q[0], y0 - 2.5 if y0 > 35 else y0 + 2.5)], 'varie', lw=0.6)
text(ax, 65, 57, r'170° : $r \approx$ 0,015', 'varie', 's')
text(ax, 65, 22, r'175° : $r \approx$ 0,004', 'varie', 's')
text(ax, 65, 14, r'180° : $r$ = 0 (pôle)', 'limite' if False else 'encre', 's')
disc(ax, p[0], p[1], 1.1, 'encre')
text(ax, 83, 31, 'O', 'encre', 's')
save(fig, '40-034')
