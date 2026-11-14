import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 69, r'$x^2-4$  avec le nombre premier  $p=2$', 'sujet', 'm')
cells = [('1', 'de $x^2$', '2 ne divise pas 1', 'resultat'),
         ('0', 'de $x$', '2 divise 0', 'resultat'),
         ('−4', 'constante', '4 divise −4', 'limite')]
for i, (c, what, res, role) in enumerate(cells):
    x = 4 + i * 28.5
    box(ax, x, 46, 25, 12, role, label=c, size='l')
    text(ax, x + 12.5, 41, what, 'fixe', 's')
    text(ax, x + 12.5, 33, res, role, 's')
    text(ax, x + 12.5, 27.5, '✓' if role == 'resultat' else '✗', role, 'l', weight='bold')
box(ax, 4, 4, 80, 14, 'limite', label=r'une condition fausse : $x^2-4=(x-2)(x+2)$', size='s')
save(fig, '54-222')
