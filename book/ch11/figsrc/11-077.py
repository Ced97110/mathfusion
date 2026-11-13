import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
s = 1.8; x = 4; base = 24
text(ax, 44, 56, r'$P = 2L + 2l$', 'sujet', 'l')
for (L, l, a) in [(12, 8, '24 + 16'), (15, 5, '30 + 10'), (10, 10, '20 + 20')]:
    w, h = L * s, l * s
    ax.add_patch(Rectangle((x, base), w, h, fc=FILL['sujet'], ec=COL['sujet'], lw=1.4, zorder=2))
    text(ax, x + w / 2, base + h + 3.5, f'{L} × {l}', 'fixe', 's')
    text(ax, x + w / 2, base - 4, a, 'sujet', 's'); text(ax, x + w / 2, base - 9, '= 40', 'resultat', 'm', weight='bold')
    x += w + 8
text(ax, 44, 6, 'même tour : 40 m', 'resultat', 'm')
save(fig, '11-077')
