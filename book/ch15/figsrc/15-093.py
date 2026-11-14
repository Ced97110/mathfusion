import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
xs, un = 14, 4.4
def rect(x, y, w, h, role): ax.add_patch(Rectangle((x, y), w, h, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
W1, H1 = xs + 3 * un, xs + 2 * un
lx, ly = 14, 22
rect(lx, ly, W1, H1, 'sujet')
text(ax, lx + W1 / 2, ly + H1 / 2, 'aire', 'sujet', 'm')
text(ax, lx + W1 / 2, 48, '$x + 3$', 'encre', 's')
text(ax, 9, ly + H1 / 2, '$x + 2$', 'encre', 's', rot=90)
text(ax, 44, ly + H1 / 2, '=', 'resultat', 'l')
rx = 58
rect(rx, ly, xs, xs, 'sujet'); rect(rx + xs, ly, 3 * un, xs, 'varie')
rect(rx, ly + xs, xs, 2 * un, 'varie'); rect(rx + xs, ly + xs, 3 * un, 2 * un, 'fixe')
text(ax, rx + xs / 2, ly + xs / 2, '$x^2$', 'sujet', 's'); text(ax, rx + xs + 1.5 * un, ly + xs / 2, '$3x$', 'varie', 's')
text(ax, rx + xs / 2, ly + xs + un, '$2x$', 'varie', 's'); text(ax, rx + xs + 1.5 * un, ly + xs + un, '$6$', 'fixe', 's')
text(ax, rx + W1 / 2, 48, '$x + 3$', 'encre', 's')
text(ax, lx + W1 / 2, 14, '$(x+2)(x+3)$', 'sujet', 's')
text(ax, rx + W1 / 2, 14, '$x^2+3x+2x+6$', 'varie', 's')
save(fig, '15-093')
