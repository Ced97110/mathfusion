import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
s = 0.9; ox, oy = 14, 16
A = (ox, oy); B = (ox + 60 * s, oy); C = (ox + 37.5 * s, oy + 33.07 * s); I = (ox + 35 * s, oy + 13.23 * s)
poly(ax, [A, B, C], 'sujet')
for V in (A, B, C): line(ax, [I, V], 'fixe', dash=True, lw=0.6)
disc(ax, *I, 13.23 * s, 'resultat', fill=False, lw=1.1)
line(ax, [I, (I[0], oy)], 'varie', lw=1.5)
disc(ax, *I, 0.9, 'varie')
text(ax, I[0], oy - 3.5, r'$r \approx 13{,}23$ m', 'varie', 's')
text(ax, 44, 52, 'trois triangles de hauteur $r$ :', 'fixe', 's')
text(ax, 44, 5, r'$\Delta = r \times s$   donc   $r = 375\sqrt{7}\,/\,75 = 5\sqrt{7}$', 'resultat', 's')
save(fig, '37-114')
