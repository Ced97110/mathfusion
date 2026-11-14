import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
k = 7.0  # mm per mm
x0, yb = 6, 12
r, h = 2, 5
cx = x0 + 2 * k
poly(ax, [(cx - r * k, yb), (cx + r * k, yb), (cx, yb + h * k)], 'sujet')
line(ax, [(cx, yb), (cx, yb + h * k)], 'varie', dash=True)
line(ax, [(cx, yb), (cx + r * k, yb)], 'varie', lw=1.4)
text(ax, cx + r * k / 2, yb - 2.8, 'r = 2 mm', 'varie', 's')
text(ax, cx - 1.5, yb + h * k / 2, 'h = 5 mm', 'varie', 's', ha='right', rot=90)
text(ax, 62, 48, 'cône', 'sujet', 'm')
text(ax, 62, 38, r'$V=\frac{1}{3}\times\pi\times 2^2\times 5$', 'sujet', 'm')
text(ax, 62, 27, '≈ 20,93 mm³', 'resultat', 'l', weight='bold')
text(ax, 62, 19, 'avec π ≈ 3,14', 'fixe', 's')
text(ax, 62, 12, 'valeur approchée', 'fixe', 's')
save(fig, '11-148')
