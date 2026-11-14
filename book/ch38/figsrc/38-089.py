import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(96)
# chaîne de triangles du nord (Paris) au sud (Perpignan) : 6 triangles
ys = [86 - 11.5 * i for i in range(7)]
pts = [(30 if i % 2 else 46, ys[i]) for i in range(7)]
for i in range(5):
    poly(ax, [pts[i], pts[i + 1], pts[i + 2]], 'fixe')
line(ax, [pts[0], pts[1]], 'sujet', lw=2.2)
line(ax, [pts[5], pts[6]], 'resultat', lw=2.2)
text(ax, 38, 93, 'Paris', 'sujet', 'm')
text(ax, 38, 9, 'Perpignan', 'resultat', 'm')
text(ax, 62, 82, 'base mesurée', 'sujet', 's', ha='left')
text(ax, 62, 78, 'environ 12 km', 'sujet', 's', ha='left')
text(ax, 58, 22, 'base de contrôle', 'resultat', 's', ha='left')
text(ax, 58, 18, 'calculée et mesurée', 'resultat', 's', ha='left')
text(ax, 58, 50, 'écart : une trentaine', 'encre', 's', ha='left')
text(ax, 58, 46, 'de centimètres', 'encre', 's', ha='left')
text(ax, 58, 42, '(0,0025 % de 12 km)', 'encre', 's', ha='left')
save(fig, '38-089')
