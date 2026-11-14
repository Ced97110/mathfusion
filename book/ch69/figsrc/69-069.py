import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
Y0 = 44
f = numberline(ax, 14, 74, Y0, -2, 0, step=1, labels=False, arrow_right=False)
g = lambda x: x ** 3 - 3 * x + 1
n = 60
pts = [(f(-2 + 2 * i / n), Y0 + 5 * g(-2 + 2 * i / n)) for i in range(n + 1)]
line(ax, pts, 'fixe', lw=1.2)
text(ax, 44, 69, 'partie 1 : on lit la courbe', 'fixe', 'm')
disc(ax, f(-2), Y0 + 5 * g(-2), 1.5, 'varie')
disc(ax, f(0), Y0 + 5 * g(0), 1.5, 'varie')
text(ax, 20, 33, r'$f(-2)=-1$', 'encre', 'm')
text(ax, 68, 58, r'$f(0)=1$', 'encre', 'm')
disc(ax, f(-1.879), Y0, 1.3, 'resultat')
text(ax, 28, 38, 'racine', 'resultat', 's')
arrow(ax, (44, 29), (44, 20.5), 'varie')
text(ax, 47, 25, 'maintenant', 'varie', 's', ha='left')
box(ax, 4, 4, 80, 16, 'resultat', label='démontré par une factorisation,\nsans continuité, dans tout corps réel clos')
save(fig, '69-069')
