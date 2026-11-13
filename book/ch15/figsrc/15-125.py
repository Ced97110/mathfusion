import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for k in range(4):
    x = 3 + k * 21
    r = 'sujet' if k == 0 else 'fixe'
    text(ax, x + 9.5, 50, f'degré {k}', r, 's')
    box(ax, x, 34, 19, 12, r, label=['8', r'$8x$', r'$8x^2$', r'$8x^3$'][k], size='m')
text(ax, 12.5, 29, 'nombre seul', 'sujet', 's')
text(ax, 44, 18, r'$8=8x^0$ car $x^0=1$', 'resultat', 'm')
text(ax, 44, 8, 'une constante : degré 0', 'resultat', 's')
save(fig, '15-125')
