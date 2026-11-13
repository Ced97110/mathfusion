import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0, y0, xw, u = 22, 12, 22, 7
def rect(x, y, w, h, role): ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
rect(x0, y0, xw, xw, 'sujet'); rect(x0 + xw, y0, 3 * u, xw, 'varie')
rect(x0, y0 + xw, xw, 2 * u, 'varie'); rect(x0 + xw, y0 + xw, 3 * u, 2 * u, 'fixe')
text(ax, x0 + xw / 2, y0 + xw / 2, '$x^2$', 'sujet', 'm')
text(ax, x0 + xw + 1.5 * u, y0 + xw / 2, '$3x$', 'varie', 'm')
text(ax, x0 + xw / 2, y0 + xw + u, '$2x$', 'varie', 'm')
text(ax, x0 + xw + 1.5 * u, y0 + xw + u, '$6$', 'fixe', 'm')
text(ax, x0 + xw / 2, 8, '$x$', 'encre', 's'); text(ax, x0 + xw + 1.5 * u, 8, '$3$', 'encre', 's')
text(ax, 18, y0 + xw / 2, '$x$', 'encre', 's'); text(ax, 18, y0 + xw + u, '$2$', 'encre', 's')
top = y0 + xw + 2 * u
brace(ax, x0, x0 + xw + 3 * u, top, 'sujet', label='$x + 3$', down=False)
line(ax, [(x0 + xw + 3 * u + 1.5, y0), (x0 + xw + 3 * u + 3, y0), (x0 + xw + 3 * u + 3, top), (x0 + xw + 3 * u + 1.5, top)], 'autre')
text(ax, x0 + xw + 3 * u + 7, (y0 + top) / 2, '$x + 2$', 'autre', 's', rot=90)
save(fig, '15-092')
