import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
cx, cy, R = 24, 36, 15
text(ax, 24, 68, r'$n=5$ côtés', 'sujet', 'm')
V = [(cx + R * math.cos(math.radians(72 * k)), cy + R * math.sin(math.radians(72 * k))) for k in range(5)]
line(ax, [(cx + R * math.cos(math.radians(t)), cy + R * math.sin(math.radians(t))) for t in range(0, 361, 5)], 'fixe', lw=0.5)
poly(ax, V, 'sujet')
labs = ['1', '$z$', '$z^2$', '$z^3$', '$z^4$']
for k, (x, y) in enumerate(V):
    disc(ax, x, y, 1.8, 'sujet')
    a = math.radians(72 * k)
    text(ax, cx + (R + 6) * math.cos(a), cy + (R + 5) * math.sin(a), labs[k], 'sujet', 's')
box(ax, 54, 46, 32, 12, 'autre', label=r'Gal de $\mathbb{Q}(z)$ : 4', size='s')
box(ax, 54, 26, 32, 12, 'resultat', label=r'$4=2\times2$ : puissance de 2', size='s')
box(ax, 54, 6, 32, 12, 'resultat', label='règle et compas', size='s')
arrow(ax, (70, 45), (70, 39), 'varie'); arrow(ax, (70, 25), (70, 19), 'varie')
save(fig, '64-193')
