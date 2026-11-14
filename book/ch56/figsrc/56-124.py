import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
y = 46
items = [(2, 26, 'fixe', r'$x^2+3x+1$', r'$a$'), (36, 15, 'sujet', r'$x+1$', r'$b$'),
         (58, 15, 'varie', r'$x+2$', r'$q$'), (78, 8, 'resultat', r'$-1$', r'$r$')]
for x, w, role, lab, name in items:
    box(ax, x, y, w, 9, role, label=lab)
    text(ax, x + w / 2, y - 4, name, role, 's')
text(ax, 31, y + 4.5, '=', 'encre', 'l')
text(ax, 54.5, y + 4.5, r'$\times$', 'encre', 'l')
text(ax, 75.5, y + 4.5, '+', 'encre', 'l')
u = 8.0
text(ax, 4, 26, r'$\delta(r)=2^0=1$', 'resultat', 's', ha='left')
box(ax, 40, 23, 1 * u, 6, 'resultat')
text(ax, 4, 14, r'$\delta(b)=2^1=2$', 'sujet', 's', ha='left')
box(ax, 40, 11, 2 * u, 6, 'sujet')
text(ax, 70, 20, r'$1<2$', 'resultat', 'm')
save(fig, '56-124')
