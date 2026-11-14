import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
base, unit = 34.0, 5.0
xs = [14, 28, 42, 56, 70]
coef = [2, -1, 0, 3, 0]
text(ax, 3, 62, r'$f = 2 - x + 3x^3$', 'sujet', 'm', ha='left')
line(ax, [(6, base), (80, base)], 'fixe', lw=0.9)
for i, (x, c) in enumerate(zip(xs, coef)):
    if c != 0:
        y0 = base if c > 0 else base + c * unit
        ax.add_patch(Rectangle((x - 4, y0), 8, abs(c) * unit, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
    if c > 0:
        text(ax, x, base + c * unit + 2.8, str(c), 'sujet', 'm')
    elif c < 0:
        text(ax, x, base + c * unit - 2.8, '−1', 'sujet', 'm')
    else:
        text(ax, x, base + 2.8, '0', 'fixe', 'm')
    text(ax, x, 19, rf'$x^{i}$', 'fixe', 's')
text(ax, 82, base + 2.8, '…', 'fixe', 'm')
text(ax, 44, 11, 'position = puissance de x', 'fixe', 's')
arrow(ax, (56, 58), (56, 54), 'varie')
text(ax, 56, 60.5, 'dernière barre : degré 3', 'varie', 's')
save(fig, '54-080')
