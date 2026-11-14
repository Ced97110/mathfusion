import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
u = 6.0
def rect(x, y, w, h, role, fill=True, lw=0.8):
    poly(ax, [(x, y), (x + w, y), (x + w, y + h), (x, y + h)], role, fill=fill, lw=lw)
x0, y0 = 4, 14
rect(x0, y0, 5 * u, 3 * u, 'sujet')            # bleu : bande 5 x 3
rect(x0, y0 + 3 * u, 3 * u, 2 * u, 'varie')    # orange : 3 x 2
rect(x0 + 3 * u, y0 + 3 * u, 2 * u, 2 * u, 'fixe', fill=False)  # petit carré b^2
ax.plot([x0 + 3 * u, x0 + 5 * u], [y0 + 3 * u, y0 + 5 * u], color=COL['fixe'], lw=0.0)
text(ax, x0 + 4 * u, y0 + 4 * u, r'$b^2$', 'fixe', 's')
brace(ax, x0, x0 + 5 * u, y0, label=r'$a=5$')
text(ax, x0 + 2.5 * u, y0 + 5 * u + 5, r'$a^2-b^2=21$', 'sujet', 's')
x1 = 42
rect(x1, y0, 5 * u, 3 * u, 'sujet')
rect(x1 + 5 * u, y0, 2 * u, 3 * u, 'varie')      # orange posée debout
arrow(ax, (x0 + 1.5 * u, y0 + 4 * u + 0), (x1 + 6 * u, y0 + 3 * u + 4), 'varie', curve=-0.35)
brace(ax, x1, x1 + 7 * u, y0, label=r'$a+b=7$')
text(ax, x1 + 3.5 * u, y0 + 3 * u + 3, r'$a-b=3$', 'sujet', 's')
text(ax, x1 + 3.5 * u, y0 + 1.5 * u, r'aire 21', 'sujet', 's')
save(fig, '21-044')
