import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(44)
f = numberline(ax, 6, 72, 20, -3, 3, labels=False, role='sujet', tick=1.6)
for v in range(-3, 4): text(ax, f(v), 15.5, f'{v}'.replace('-', '−'), 'sujet', 's')
text(ax, 82, 24, r'$x$', 'sujet', 'l')
brace(ax, 6, f(0) - 1, 27, 'fixe', 'à gauche de 0', down=False); brace(ax, f(0) + 1, 72, 27, 'fixe', 'à droite de 0', down=False)
text(ax, 44, 6, 'on y lit le 1er nombre du couple', 'sujet', 's')
text(ax, 44, 40, r'axe des $x$', 'sujet', 'l')
save(fig, '19-013')
