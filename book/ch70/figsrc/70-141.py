import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
labels = [(80, 'fixe', r'$\partial f/\partial y=2y$'),
          (68, 'fixe', r'$\partial f/\partial x=1-3(x-2)^2$'),
          (56, 'fixe', r'$q=2xy-y\,(1-3(x-2)^2)$'),
          (42, 'sujet', r'$q=y\,k(x)$'),
          (14, 'resultat', r'en $x=1$ : $q=4y$')]
for y, role, lab in labels:
    box(ax, 3, y, 50, 9, role, label=lab, size='s')
for y in (80, 68, 56):
    arrow(ax, (28, y), (28, y - 3), 'varie', lw=1.0)
text(ax, 28, 37, r'$k(x)=3x^2-10x+11$', 'sujet', 's')
text(ax, 28, 30, r'$k(1)=3-10+11=4$', 'resultat', 's')
arrow(ax, (28, 27), (28, 23), 'resultat', lw=1.0)
ox, oy = 71, 52
line(ax, [(ox - 14, oy), (ox + 14, oy)], 'fixe', lw=0.7)
line(ax, [(ox, oy - 16), (ox, oy + 18)], 'fixe', lw=0.7)
line(ax, [(ox - 12, oy - 12), (ox + 12, oy + 12)], 'sujet', lw=1.5)
disc(ax, ox, oy, 1.4, 'resultat')
text(ax, ox, oy + 22, r'$q$, degré 1 en $y$', 'sujet', 's')
text(ax, ox + 14, oy - 3, r'$y$', 'fixe', 's')
text(ax, ox + 8, oy - 9, 'racine\n$y=0$', 'resultat', 's')
save(fig, '70-141')
