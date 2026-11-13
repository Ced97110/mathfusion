import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 7.0
def row(y, tot, parts, caption, crole):
    text(ax, 3, y + 4, f'{tot} = ' + ' + '.join(str(p) for p in parts), 'encre', 'l', ha='left')
    x = 27
    for d in parts:
        role = crole if (crole == 'limite' or d == 1) else 'fixe'
        box(ax, x, y, d * u - 1.0, 8, role, label=str(d), size='m')
        x += d * u
    text(ax, x + 3, y + 4, caption, crole, 's', ha='left')
row(46, 3, (1, 2), 'racine garantie', 'resultat')
row(32, 4, (2, 2), 'pas de racine garantie', 'limite')
box(ax, 4, 4, 80, 12, 'limite', label=r'$x^4+3x^2+2=(x^2+1)(x^2+2)$', size='m')
text(ax, 44, 21, 'sans facteur de degré 1', 'limite', 's')
save(fig, '54-210')
