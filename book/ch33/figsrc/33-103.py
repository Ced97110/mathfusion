import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
y = 18
f = numberline(ax, 8, 68, y, -90, 180, step=30, every=3)
ax.add_patch(Rectangle((f(-90), y - 1.2), f(90) - f(-90), 2.4, fc=FILL['resultat'], ec=COL['resultat'], lw=0.8, zorder=1))
text(ax, f(0), 8, r'$[-90°\,;\,90°]$', 'resultat', 's')
disc(ax, f(150), y, 1.8, 'sujet'); disc(ax, f(30), y, 1.8, 'autre')
text(ax, f(150), y + 6, '150°', 'sujet', 'm'); text(ax, f(30), y + 6, '30°', 'autre', 'm')
arrow(ax, (f(150) - 2, y + 9), (f(30) + 2, y + 9), 'varie', curve=0.35)
text(ax, f(90), y + 18, 'sin puis arcsin', 'varie', 's')
text(ax, f(90), y + 24, r'$30° \neq 150°$', 'limite', 'm')
save(fig, '33-103')
