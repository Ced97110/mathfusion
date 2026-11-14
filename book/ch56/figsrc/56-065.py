import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
box(ax, 30, 70, 28, 11, 'fixe', label=r'$x^2y^2$')
# left factorization (violet), right factorization (blue)
for x0, role, labs in [(4, 'autre', [r'$x^2$', r'$y^2$']), (50, 'sujet', [r'$xy$', r'$xy$'])]:
    for i, l in enumerate(labs):
        box(ax, x0 + i * 20, 50, 15, 10, role, label=l)
    text(ax, x0 + 17.5, 55, r'$\times$', 'encre')
arrow(ax, (38, 70), (21.5, 61), 'autre')
arrow(ax, (50, 70), (67.5, 61), 'sujet')
text(ax, 67.5, 43, r'$xy\mid x^2y^2$ : oui', 'resultat', 'm')
box(ax, 4, 6, 80, 22, 'limite', fill=False, dash=True)
text(ax, 44, 21, r'$xy$ ne divise pas $x^2$', 'limite', 'm')
text(ax, 44, 12, r'quotient $x/y$ : pas polynôme', 'limite', 's')
save(fig, '56-065')
