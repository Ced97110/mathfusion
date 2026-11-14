import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
u, y0 = 1.4, 12
steps = [(10, r'$A$', 'sujet'), (8, r'$B$', 'sujet'), (6, r'$C$', 'sujet'),
         (-3, r'$A\cap B$', 'limite'), (-2, r'$A\cap C$', 'limite'), (-1, r'$B\cap C$', 'limite'),
         (1, r'$A\cap B\cap C$', 'varie')]
tot = 0; prev_x = None
for i, (d, name, role) in enumerate(steps):
    x = 3 + 10.4 * i
    a, b = tot, tot + d
    lo, hi = min(a, b), max(a, b)
    ax.add_patch(Rectangle((x, y0 + lo * u), 7.5, (hi - lo) * u, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    s = ('+' if d > 0 else '−') + str(abs(d))
    text(ax, x + 3.75, y0 + hi * u + 3.4, s + '\n' + name, role, 's')
    if i > 0: line(ax, [(x - 2.1, y0 + a * u), (x, y0 + a * u)], 'fixe', lw=0.6, dash=True)
    tot = b
x = 3 + 10.4 * 7
line(ax, [(x - 2.1, y0 + tot * u), (x, y0 + tot * u)], 'fixe', lw=0.6, dash=True)
ax.add_patch(Rectangle((x, y0), 7.5, tot * u, ec=COL['resultat'], fc=FILL['resultat'], lw=0.8, zorder=2))
text(ax, x + 3.75, y0 + tot * u + 3.4, '= ' + str(tot) + '\ntotal', 'resultat', 's')
line(ax, [(2, y0), (84, y0)], 'fixe', lw=0.8)
save(fig, '80-355')
