import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
xs = [12, 44, 76]; y = 78
labs = [r'$\alpha$', r'$\alpha^2$', r'$\alpha^2+\alpha$']
for x, s in zip(xs, labs): box(ax, x - 9, y - 5, 18, 10, 'sujet', label=s)
arrow(ax, (xs[0] + 10, y), (xs[1] - 10, y), 'varie'); arrow(ax, (xs[1] + 10, y), (xs[2] - 10, y), 'varie')
arrow(ax, (xs[2], y - 6), (xs[0], y - 6), 'resultat', curve=-0.45)
text(ax, 27, y + 3.5, '1', 'varie', 's'); text(ax, 60, y + 3.5, '2', 'varie', 's')
text(ax, 44, 54, r'3 : retour à $\alpha$', 'resultat', 's')
calc = [r'1 : $\varphi(\alpha)=\alpha^2$',
        r'2 : $\alpha^4=\alpha\cdot\alpha^3=\alpha^2+\alpha$',
        r'3 : $\alpha^4+\alpha^2=\alpha^2+\alpha+\alpha^2=\alpha$']
for i, s in enumerate(calc): text(ax, 4, 40 - i * 9, s, 'sujet', 's', ha='left')
text(ax, 44, 8, r'règle du cube : $\alpha^3=\alpha+1$', 'fixe', 's')
save(fig, '67-094')
