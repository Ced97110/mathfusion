import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
r = 2 ** 0.5
assert abs(r ** 2 - 2) < 1e-12 and abs(r ** 4 - 4) < 1e-12
f = numberline(ax, 10, 70, 14, 0, 3, arrow_right=True)
disc(ax, f(r), 14, 2.2, 'sujet')
text(ax, 16, 20, r'$u=\sqrt{2}$', 'sujet', 'm')
box(ax, 4, 40, 36, 12, 'resultat', label=r'$x^2-2$', size='m')
box(ax, 46, 40, 36, 12, 'resultat', label=r'$x^4-4$', size='m')
arrow(ax, (22, 39.5), (f(r) - 1.5, 17.5), 'varie')
arrow(ax, (64, 39.5), (f(r) + 1.5, 17.5), 'varie')
text(ax, 22, 56, r'$(\sqrt{2})^2-2=0$', 'resultat', 's')
text(ax, 64, 56, r'$(\sqrt{2})^4-4=0$', 'resultat', 's')
text(ax, 44, 30, 's’annulent en $u$', 'varie', 's')
save(fig, '54-116')
