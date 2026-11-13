import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
xs = [10, 19, 28, 37, 46, 55, 76]
def ground(y):
    line(ax, [(6, y), (60, y)], 'fixe'); line(ax, [(60, y), (70, y)], 'fixe', dash=True); line(ax, [(70, y), (82, y)], 'fixe')
ground(46)
for i, x in enumerate(xs):
    r = 'varie' if i == 0 else 'fixe'
    ax.add_patch(Rectangle((x - 1.2, 46), 2.4, 9, ec=COL[r], fc=FILL[r] if i == 0 else COL['fixe'], lw=0.6, zorder=2))
arrow(ax, (3, 52), (8.5, 52), 'varie')
text(ax, 24, 64, 'départ : on pousse le 0', 'varie', 's')
for x in xs[:5]: arrow(ax, (x + 1.2, 56), (x + 7.8, 56), 'varie', curve=-0.5)
text(ax, 62, 64, 'passage : touche le suivant', 'varie', 's')
ground(18)
for x in xs:
    poly(ax, [(x + 1.2, 18), (x + 0.19, 20.18), (x + 8.34, 23.98), (x + 9.36, 21.80)], 'resultat')
for i, x in enumerate(xs): text(ax, x, 14.6, '4 329' if i == 6 else str(i), 'fixe', 's')
text(ax, 44, 34, 'tous tombent, même 4 329', 'resultat', 'm')
save(fig, '01-120')
