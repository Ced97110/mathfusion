import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(94)
box(ax, 4, 80, 80, 10, 'sujet', label=r'$f=x^3-3x+1$')
arrow(ax, (17, 80), (17, 75.5), 'fixe')
rows = [(64, r'$x^3$', r'$3x^2$', 'exposant devant,\npuis −1'),
        (48, r'$-3x$', r'$-3$', r'le $x$ disparaît'),
        (32, r'$1$', 'rien', 'disparaît')]
for k, (y, a, b, lab) in enumerate(rows):
    box(ax, 4, y, 26, 11, 'sujet', label=a)
    if k < 2:
        box(ax, 58, y, 26, 11, 'resultat', label=b)
    else:
        box(ax, 58, y, 26, 11, 'fixe', label=b, dash=True)
    arrow(ax, (30.5, y + 2.5), (57.5, y + 2.5), 'varie')
    text(ax, 44, y + 7.5, lab, 'varie', 's')
arrow(ax, (71, 32), (71, 19.5), 'resultat')
box(ax, 4, 8, 80, 11, 'resultat', label=r"$f'=3x^2-3$")
save(fig, '69-083')
