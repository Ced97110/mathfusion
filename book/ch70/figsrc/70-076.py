import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'$f=x^2y+y^3$', 'encre', 'l')
cols = [(2, 'sujet', r'on fixe $y=1$', r'$x^2+1$', r'$2x$', r'dérive en $x$',
         r'$\partial f/\partial x=2xy$'),
        (46, 'autre', r'on fixe $x=2$', r'$4y+y^3$', r'$4+3y^2$', r'dérive en $y$',
         r'$\partial f/\partial y=x^2+3y^2$')]
for x, role, fix, b1, b2, act, gen in cols:
    c = x + 20
    text(ax, c, 65, fix, 'fixe', 's')
    box(ax, x, 48, 40, 11, 'fixe', label=b1)
    arrow(ax, (c, 47.5), (c, 37.5), 'varie')
    text(ax, c + 2.5, 42.5, act, 'varie', 's', ha='left')
    box(ax, x, 26, 40, 11, role, label=b2)
    text(ax, c, 15, gen, 'resultat', 's')
save(fig, '70-076')
