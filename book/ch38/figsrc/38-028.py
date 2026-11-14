import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(56)
g = 24.0
# Gauche : la tour, un seul triangle rectangle (d mesurée)
d1 = 18.0; h1 = d1 * math.tan(math.radians(40))
E = (5, g); H1 = (E[0] + d1, g); S1 = (H1[0], g + h1)
poly(ax, [E, H1, S1], 'sujet')
line(ax, [(E[0] - 2, g), (H1[0] + 3, g)], 'fixe')
line(ax, [(H1[0] - 2.2, g), (H1[0] - 2.2, g + 2.2), (H1[0], g + 2.2)], 'fixe', lw=0.7)
text(ax, 14.5, g - 3.5, '50 m mesurés', 'sujet', 's')
text(ax, 15, g + h1 + 6, 'tour', 'sujet', 'm', weight='bold')
text(ax, 15, g + h1 + 2.5, '1 triangle', 'sujet', 's')
# Droite : la montagne, deux triangles (seule AB est mesurée)
h = 14.0
xs = 84.0
A = (xs - h / math.tan(math.radians(18)), g)
B = (xs - h / math.tan(math.radians(21.25)), g)
S = (xs, g + h)
poly(ax, [A, B, S], 'autre')
poly(ax, [B, (xs, g), S], 'sujet')
line(ax, [(A[0] - 3, g), (xs + 3, g)], 'fixe')
line(ax, [(B[0], g - 1.6), (xs, g - 1.6)], 'fixe', dash=True, lw=1.1)
text(ax, (B[0] + xs) / 2, g - 4.5, 'B → pied : dans la roche', 'fixe', 's')
text(ax, 62, g + h + 6, 'montagne', 'sujet', 'm', weight='bold')
text(ax, 62, g + h + 2.5, '2 triangles', 'sujet', 's')
line(ax, [(33, 10), (33, 50)], 'fixe', dash=True, lw=0.6)
save(fig, '38-028')
