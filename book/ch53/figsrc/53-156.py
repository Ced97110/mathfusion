import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
X0, Y0, S = 14.0, 8.0, 1.2   # origine du graphique, mm par unité
box(ax, X0, Y0, 55 * S, 55 * S, 'fixe', fill=False, lw=0.6, r=0.1)
sel = {8: 17, 9: 14, 10: 10}
for m in range(0, 55):
    c = pow(m, 3, 55)
    if m in sel: continue
    ax.add_patch(Circle((X0 + m * S, Y0 + c * S), 0.55, fc=COL['fixe'], ec='none', zorder=2.5))
for m, c in sel.items():
    ax.add_patch(Circle((X0 + m * S, Y0 + c * S), 0.9, fc=COL['varie'], ec='none', zorder=3))
# étiquettes des trois voisins, reliées par un trait
for (m, c), lx in zip(sel.items(), (X0 + 4, X0 + 24, X0 + 44)):
    line(ax, [(X0 + m * S, Y0 + c * S), (lx, Y0 + 55 * S + 4)], 'varie', lw=0.5)
    text(ax, lx, Y0 + 55 * S + 7, f'({m}, {c})', 'varie', 's')
for v in (0, 20, 40):
    text(ax, X0 + v * S, Y0 - 2.5, str(v), 'fixe', 's')
    if v: text(ax, X0 - 3, Y0 + v * S, str(v), 'fixe', 's')
text(ax, X0 + 66, Y0 - 2.5, r'$m$', 'sujet', 'm')
text(ax, 3, Y0 + 28 * S, r'$m^{3}$', 'sujet', 'm')
save(fig, '53-156')
