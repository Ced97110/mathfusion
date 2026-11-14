import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
cx, cy, R = 24, 40, 14
text(ax, 24, 70, r'$x^5=1$', 'sujet', 'l')
line(ax, [(cx + R * math.cos(math.radians(t)), cy + R * math.sin(math.radians(t))) for t in range(0, 361, 5)], 'fixe', lw=0.5)
labs = ['1', '$z$', '$z^2$', '$z^3$', '$z^4$']
for k in range(5):
    a = math.radians(72 * k)
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 2, 'fixe' if k == 0 else 'sujet')
    text(ax, cx + (R + 6) * math.cos(a) - (1 if k == 0 else 0), cy + (R + 5) * math.sin(a), labs[k], 'fixe' if k == 0 else 'sujet', 's')
box(ax, 58, 48, 26, 11, 'sujet', label=r'$\mathbb{Q}(z)$')
box(ax, 58, 20, 26, 11, 'sujet', label=r'$\mathbb{Q}$')
arrow(ax, (71, 32), (71, 47), 'varie')
text(ax, 62, 39.5, 'un seul\nradical', 'varie', 's', ha='right')
text(ax, 44, 6, r'$G\supset\{e\}$ : un seul étage', 'resultat', 'm')
save(fig, '64-186')
