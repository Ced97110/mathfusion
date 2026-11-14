import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 32, 60, r'sur $\mathbb{R}$ : $f=\lambda^2+1$', 'sujet', 'm')
f = numberline(ax, 4, 60, 14, -2, 2, arrow_right=False)
xs = [i / 20 for i in range(-40, 41)]
line(ax, [(f(x), 14 + 7 * (x * x + 1)) for x in xs], 'sujet', lw=1.4)
text(ax, 32, 6, 'ne touche pas l’axe', 'limite', 's')
text(ax, 32, 52, 'aucune racine réelle', 'limite', 's')
text(ax, 74, 40, r'sur $\mathbb{C}$ :', 'resultat', 's')
text(ax, 74, 33, r'$(\lambda-i)(\lambda+i)$', 'resultat', 's')
text(ax, 74, 26, 'degré 1', 'resultat', 's')
save(fig, '60-178')
