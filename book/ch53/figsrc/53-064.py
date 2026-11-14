import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle

n = 600
e_count = n // 6
equal = n / 26
assert e_count == 100 and 23 < equal < 23.1

fig, ax = canvas(72)
s, base = 0.4, 14
text(ax, 44, 68, '600 lettres de français', 'encre', 'm')
ax.add_patch(Rectangle((14, base), 16, e_count * s, fc=FILL['sujet'], ec=COL['sujet'], lw=0.8, zorder=2))
ax.add_patch(Rectangle((46, base), 16, equal * s, fc=FILL['fixe'], ec=COL['fixe'], lw=0.8, zorder=2))
line(ax, [(6, base + equal * s), (66, base + equal * s)], 'varie', dash=True)
line(ax, [(6, base), (80, base)], 'fixe')
text(ax, 22, base + e_count * s + 3, '≈ 100', 'sujet', 'm')
text(ax, 54, base + equal * s + 3, '≈ 23', 'fixe', 'm')
text(ax, 22, 8, 'E : une lettre\nsur six', 'sujet', 's')
text(ax, 62, 8, 'chaque lettre,\nsi toutes égales', 'fixe', 's')
save(fig, '53-064')
