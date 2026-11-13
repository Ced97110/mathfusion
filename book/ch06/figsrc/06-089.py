import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
rows = ((42, r'$\frac{18}{24}$', r'$\div 6$', 'sujet', 'avec des nombres'),
        (17, r'$\frac{6x}{8x}$', r'$\div 2x$', 'autre', 'avec une lettre'))
for y, a, d, r, lab in rows:
    text(ax, 16, y + 11, lab, r, 's')
    text(ax, 16, y, a, r, 'l')
    arrow(ax, (28, y), (58, y), 'varie')
    text(ax, 43, y + 3.5, d, 'varie', 's')
    text(ax, 70, y, r'$\frac{3}{4}$', 'resultat', 'l')
text(ax, 44, 4, r'$x\neq 0$', 'limite', 's')
save(fig, '06-089')
