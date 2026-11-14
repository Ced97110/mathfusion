import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
base, unit = 36.0, 4.0
panels = [(15, 'nulle', 'fixe', [0, 0, 0, 0, 0, 0], '(0, 0, 0, …)', 'que des zéros'),
          (44, 'presque nulle', 'sujet', [3, 0, 0, 2, 0, 0], '(3, 0, 0, 2, 0, …)', 'zéros dès le rang 4'),
          (73, 'quelconque', 'limite', [1, 1, 1, 1, 1, 1], '(1, 1, 1, …)', 'jamais de zéros')]
for cx, title, role, vals, seq, cap in panels:
    text(ax, cx, 57, title, role, 'm', weight='bold')
    x0 = cx - 10
    line(ax, [(x0 - 2, base), (x0 + 22, base)], 'fixe', lw=0.8)
    for i, v in enumerate(vals):
        x = x0 + 4 * i
        if v:
            ax.add_patch(Rectangle((x - 1.5, base), 3, v * unit, ec=COL[role], fc=FILL[role], lw=0.7, zorder=2))
        else:
            disc(ax, x, base, 0.6, role)
    text(ax, cx, 29, seq, role, 's')
    text(ax, cx, 21, cap, role, 's')
line(ax, [(44 - 10 + 14, base - 3), (44 - 10 + 14, base + 14)], 'resultat', dash=True)
save(fig, '54-083')
