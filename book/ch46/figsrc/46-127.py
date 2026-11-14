import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 6, 78, 26, 0, 24, step=4, labels=False, arrow_right=False)
for v in (12, 24):
    disc(ax, f(v), 26, 1.7, 'fixe')
    text(ax, f(v), 19, str(v), 'fixe', 's')
for v in (0, 8, 16):
    disc(ax, f(v), 26, 1.7, 'sujet')
    text(ax, f(v), 19, str(v), 'sujet', 's')
disc(ax, f(24), 26, 1.7, 'resultat')
for v in (0, 8, 16):
    arrow(ax, (f(v) + 1.8, 28), (f(v + 8) - 1.8, 28), 'varie', curve=-0.45)
    text(ax, f(v + 4), 38, '+ 8', 'varie', 's')
text(ax, f(8), 12, r'$b$', 'sujet', 's')
text(ax, f(16), 12, r'$b^2$', 'sujet', 's')
text(ax, f(24) - 2, 12, r'$b^3 = e$', 'resultat', 's')
text(ax, 44, 52, r'$n$ = 12, $k$ = 8, $d$ = 4 : ordre 3', 'encre', 'm')
text(ax, 44, 4, 'gris : multiples de 12 (tours)', 'fixe', 's')
save(fig, '46-127')
