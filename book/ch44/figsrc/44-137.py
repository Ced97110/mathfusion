import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
s = 16; xs = [16, 44, 72]; cy = 28; tops = [True, False, True]
for k, x in enumerate(xs):
    poly(ax, [(x - s/2, cy - s/2), (x + s/2, cy - s/2), (x + s/2, cy + s/2), (x - s/2, cy + s/2)], 'sujet')
    line(ax, [(x - s/2 - 2, cy), (x + s/2 + 2, cy)], 'fixe', lw=0.8, dash=True)
    disc(ax, x - s/2 + 3, cy + (s/2 - 3 if tops[k] else -s/2 + 3), 2.2, 'varie')
    text(ax, x, 12, ['départ', r'après $s$', r'après $s$, $s$'][k], 'sujet' if k < 2 else 'resultat', 's')
arrow(ax, (25.5, 28), (33, 28), 'varie', lw=1.3); arrow(ax, (53.5, 28), (61, 28), 'varie', lw=1.3)
text(ax, 29.5, 33, r'$s$', 'varie', 'm'); text(ax, 57.5, 33, r'$s$', 'varie', 'm')
text(ax, 44, 44, r'axe de $s$ (pointillés)', 'fixe', 's')
text(ax, 44, 4, r'$s^2 = 1$ : retour au départ', 'resultat', 'm')
save(fig, '44-137')
