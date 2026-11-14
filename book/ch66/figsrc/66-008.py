import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
y = 30
f = numberline(ax, 8, 68, y, 0, 4)
disc(ax, f(math.sqrt(2)), y, 1.5, 'resultat'); disc(ax, f(2), y, 1.5, 'resultat'); disc(ax, f(math.pi), y, 1.5, 'limite')
box(ax, 2, 46, 38, 9, 'resultat', label=r'$\sqrt{2}$ : racine de $x^2-2$', size='s')
box(ax, 46, 46, 38, 9, 'resultat', label=r'2 : racine de $x-2$', size='s')
arrow(ax, (f(math.sqrt(2)), 46), (f(math.sqrt(2)), y + 2), 'resultat')
arrow(ax, (50, 46), (f(2) + 0.6, y + 2), 'resultat')
box(ax, 38, 6, 48, 13, 'limite', label=r'$\pi\approx3{,}14159$ :' + '\naucun polynôme', size='s')
arrow(ax, (f(math.pi), 19.5), (f(math.pi), y - 2), 'limite')
text(ax, 20, 12, 'Lindemann, 1882', 'fixe', 's')
save(fig, '66-008')
