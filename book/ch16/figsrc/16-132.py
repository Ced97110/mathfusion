import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
f = numberline(ax, 12, 72, 8, 2, 5, 1, arrow_right=False, size='m')
Y = lambda v: 8 + (v - 3.5) * 11.0
line(ax, [(f(2), Y(5)), (f(5), Y(8))], 'sujet', lw=1.6)
line(ax, [(f(2), Y(7)), (f(5), Y(7))], 'varie', lw=1.6)
for v in (2, 3, 5):
    disc(ax, f(v), Y(v + 3), 1.1, 'sujet')
    text(ax, f(v) + (-3 if v < 4 else 3), Y(v + 3) + (-3 if v < 4 else 3), str(v + 3), 'sujet', 's')
disc(ax, f(4), Y(7), 1.6, 'resultat')
line(ax, [(f(4), 10), (f(4), Y(7))], 'resultat', dash=True)
text(ax, f(4), Y(7) + 5, r'$x$ = 4', 'resultat', 'm')
text(ax, 3, 58, r'membre de gauche : $x$ + 3', 'sujet', 's', ha='left'); text(ax, 85, Y(7) - 4, 'membre de droite : 7', 'varie', 's', ha='right')
text(ax, f(4) + 2, 32, 'elles se rencontrent', 'resultat', 's', ha='left')
text(ax, 79, 8, r'$x$', 'fixe', 'm')
save(fig, '16-132')
