import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
u = 3.6
def R(x, y, w, h, r, lab=None, sz='m'): box(ax, x, y, w * u, h * u, r, label=lab, r=0.3, size=sz)
x0, y0 = 4, 12
R(x0, y0, 5, 2, 'sujet', 'P'); R(x0, y0 + 2 * u, 2, 3, 'varie', 'Q')
x1 = 50
R(x1, y0, 5, 2, 'sujet', 'P'); R(x1 + 5 * u, y0, 3, 2, 'varie', 'Q')
arrow(ax, (x0 + 1 * u, y0 + 5.2 * u), (x1 + 6.5 * u, y0 + 2.4 * u), 'varie', curve=-0.35)
text(ax, 40, 30, 'on tourne Q', 'varie', 'm', weight='bold')
text(ax, x0 + 6 * u, y0 + 2.6 * u, r'hauteur $b$ avant', 'limite', 's', ha='left')
text(ax, x1 + 8 * u + 1.5, y0 + 1 * u, r'$a-b$', 'resultat', 'm', ha='left')
brace(ax, x1, x1 + 8 * u, y0 - 0.5, 'resultat', r'largeur $a+b$', size='s')
save(fig, '18-053')
