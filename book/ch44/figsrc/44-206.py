import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
comp = lambda a, b: tuple(a[b[x]] for x in range(3))
e = (0, 1, 2); sg = (1, 2, 0); sg2 = comp(sg, sg)
t1 = (0, 2, 1); t2 = (2, 1, 0); t3 = (1, 0, 2)
els = [e, sg, sg2, t1, t2, t3]
names = ['$e$', r'$\sigma$', r'$\sigma^2$', r'$\tau_1$', r'$\tau_2$', r'$\tau_3$']
roles = ['fixe', 'sujet', 'varie', 'resultat', 'autre', 'limite']
c = 8; x0, y0 = 22, 10
for i in range(6):
    box(ax, x0 + i * c, y0 + 6 * c, c, c, roles[i], label=names[i], size='s', r=0.3)
    box(ax, x0 - c, y0 + (5 - i) * c, c, c, roles[i], label=names[i], size='s', r=0.3)
    for j in range(6):
        k = els.index(comp(els[i], els[j]))
        box(ax, x0 + j * c, y0 + (5 - i) * c, c, c, roles[k], r=0.3)
line(ax, [(x0, y0 + 6 * c), (x0 + 6 * c, y0)], 'encre', lw=0.7, dash=True)
ctr = lambda i, j: (x0 + j * c + c / 2, y0 + (5 - i) * c + c / 2)
for (i, j) in [(3, 1), (1, 3)]:
    p = ctr(i, j)
    ax.add_patch(Rectangle((p[0] - c / 2, p[1] - c / 2), c, c, fill=False, ec=COL['encre'], lw=1.6, zorder=6))
ri, cj = 4, 2
ax.add_patch(Rectangle((x0, y0 + (5 - ri) * c), 6 * c, c, fill=False, ec=COL['varie'], lw=2.0, zorder=7))
ax.add_patch(Rectangle((x0 + cj * c, y0), c, 6 * c, fill=False, ec=COL['varie'], lw=2.0, zorder=7))
text(ax, 78, 10, 'diagonale', 'encre', 's')
text(ax, 44, 4, 'ligne et colonne orange : 6 couleurs', 'varie', 's')
save(fig, '44-206')
