import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
def nd(x, y, s, role):
    box(ax, x - 6, y - 4, 12, 8, role, label=s, size='s')
Z = r'$\{0\}$'
L = {'0': (16, 12, Z, 'fixe'), '4': (6, 30, r'$\langle4\rangle$', 'fixe'), '6': (26, 30, r'$\langle6\rangle$', 'sujet'),
     '3': (36, 42, r'$\langle3\rangle$', 'sujet'), '2': (16, 52, r'$\langle2\rangle$', 'sujet'), 'G': (26, 68, r'$G$', 'sujet')}
for a, b in [('0', '4'), ('0', '6'), ('6', '3'), ('6', '2'), ('4', '2'), ('3', 'G'), ('2', 'G')]:
    ax.plot(*zip(L[a][:2], L[b][:2]), color=COL['fixe'], lw=0.9, zorder=1)
for k, (x, y, s, r) in L.items(): nd(x, y, s, r)
R = {'6': (68, 30, Z), '3': (78, 42, r'$\langle3\rangle$'), '2': (58, 52, r'$\langle2\rangle$'), 'G': (68, 68, r'$G/K$')}
for a, b in [('6', '3'), ('6', '2'), ('3', 'G'), ('2', 'G')]:
    ax.plot(*zip(R[a][:2], R[b][:2]), color=COL['autre'], lw=0.9, zorder=1)
for k, (x, y, s) in R.items():
    nd(x, y, s, 'autre'); arrow(ax, (L[k][0] + 6.5, L[k][1]), (x - 6.5, y), 'varie')
text(ax, 22, 79, r'$G=\mathbb{Z}/12\mathbb{Z}$', 'sujet', 's', weight='bold')
text(ax, 68, 79, r'$G/K$', 'autre', 's', weight='bold')
text(ax, 66, 10, 'gris : sans $K$', 'fixe', 's')
save(fig, '48-094')
