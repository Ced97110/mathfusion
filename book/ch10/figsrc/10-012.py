import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(70)
def wave(cx, y, role, lw=1.6):
    xs = np.linspace(cx - 6, cx + 6, 40)
    for dy in (1.8, -1.8): ax.plot(xs, y + dy + 0.9 * np.sin((xs - cx + 6) / 12 * 2 * np.pi), color=COL[role], lw=lw, zorder=3)
text(ax, 15, 62, 'estimation', 'varie', 's'); text(ax, 73, 62, 'somme vraie', 'resultat', 's')
text(ax, 15, 54, '8 500', 'varie', 'l'); text(ax, 73, 54, '8 463', 'resultat', 'l')
wave(44, 54, 'sujet')
text(ax, 44, 44, 'proches, écart 37', 'sujet', 'm')
text(ax, 15, 28, '8 500', 'limite', 'l'); text(ax, 73, 28, '8 463', 'limite', 'l')
for dy in (1.8, -1.8): line(ax, [(38, 28 + dy), (50, 28 + dy)], 'limite', lw=1.6)
line(ax, [(39, 22), (49, 34)], 'limite', lw=1.2)
text(ax, 44, 12, 'faux : pas le même nombre', 'limite', 'm')
save(fig, '10-012')
