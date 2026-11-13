import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle

assert 26 * 26 == 676
word = 'ALGEBRE'
pairs = [word[0:2], word[2:4], word[4:6], word[6:]]
assert pairs == ['AL', 'GE', 'BR', 'E']

fig, ax = canvas(94)
text(ax, 44, 90, 'Léa chiffre ALGEBRE par paires', 'encre', 'm')
for i, p in enumerate(pairs):
    box(ax, 10 + i * 18, 72, 15, 10, 'varie' if len(p) == 2 else 'fixe', label=p)
u = 1.3
ax.add_patch(Rectangle((6, 52), 26 * u, u, fc=FILL['sujet'], ec=COL['sujet'], lw=0.5, zorder=2))
for k in range(27):
    ax.plot([6 + k * u] * 2, [52, 52 + u], color=COL['sujet'], lw=0.25, zorder=3)
text(ax, 6 + 13 * u, 57, '26 lettres', 'sujet', 's')
text(ax, 6 + 13 * u, 36, 'chaque paire est\nplus rare qu’une lettre', 'fixe', 's')
gx, gy = 49, 18
ax.add_patch(Rectangle((gx, gy), 26 * u, 26 * u, fc=FILL['autre'], ec=COL['autre'], lw=0.6, zorder=2))
for k in range(27):
    ax.plot([gx + k * u] * 2, [gy, gy + 26 * u], color=COL['autre'], lw=0.2, zorder=3)
    ax.plot([gx, gx + 26 * u], [gy + k * u] * 2, color=COL['autre'], lw=0.2, zorder=3)
text(ax, gx + 13 * u, gy + 26 * u + 4, '676 paires', 'autre', 's')
text(ax, gx + 13 * u, gy - 4, r'$26 \times 26 = 676$', 'autre', 's')
save(fig, '53-068')
