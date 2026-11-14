import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
# haut : les deux racines possibles de x^2 + x - 1, choix par le signe
text(ax, 44, 80, r'deux racines de $x^2 + x - 1$', 'encre', 'm')
ux, X0, Y = 20, 56, 66
fx = lambda v: X0 + ux * v
arrow(ax, (fx(-2.3), Y), (fx(1.3), Y), 'fixe', lw=0.8)
line(ax, [(fx(0), Y - 1.5), (fx(0), Y + 1.5)], 'fixe')
text(ax, fx(0), Y - 4, '0', 'fixe', 's')
ax.add_patch(Rectangle((fx(0), Y - 0.9), fx(1.3) - fx(0), 1.8, fc=FILL['resultat'], ec='none', zorder=1))
r = (-1 + math.sqrt(5)) / 2; t = (-1 - math.sqrt(5)) / 2
disc(ax, fx(r), Y, 1.5, 'resultat'); disc(ax, fx(t), Y, 1.5, 'limite')
text(ax, fx(r), Y + 5, r'$\frac{-1+\sqrt{5}}{2} > 0$', 'resultat', 's')
text(ax, fx(t), Y + 5, r'$\frac{-1-\sqrt{5}}{2} < 0$', 'limite', 's')
# bas : quart de cercle, cos 72°
cx, cy, R = 14, 6, 38
a = math.radians(72)
th = [math.radians(d) for d in range(0, 91, 3)]
line(ax, [(cx + R * math.cos(v), cy + R * math.sin(v)) for v in th], 'fixe', lw=0.7)
line(ax, [(cx, cy), (cx + R + 2, cy)], 'fixe', lw=0.7)
line(ax, [(cx, cy), (cx, cy + R + 2)], 'fixe', lw=0.7)
wx, wy = cx + R * math.cos(a), cy + R * math.sin(a)
line(ax, [(cx, cy), (wx, wy)], 'sujet')
line(ax, [(wx, wy), (wx, cy)], 'varie', dash=True)
disc(ax, wx, wy, 1.4, 'sujet')
line(ax, [(cx, cy - 1.4), (wx, cy - 1.4)], 'resultat', lw=1.6)
text(ax, (cx + wx) / 2, cy - 4.5, r'$\cos 72°$', 'resultat', 's')
text(ax, wx + 2, wy + 1, r'$\omega$', 'sujet', 'm', ha='left')
text(ax, 58, 38, r'$s = 2\cos 72° > 0$', 'resultat', 'm')
text(ax, 58, 28, 'donc $s$ est la racine positive', 'resultat', 's')
text(ax, 58, 15, r'$\cos 72° = \frac{\sqrt{5}-1}{4}$', 'resultat', 'l')
save(fig, '63-169')
