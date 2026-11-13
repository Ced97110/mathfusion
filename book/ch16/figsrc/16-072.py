import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
f = numberline(ax, 10, 74, 18, 0, 12, every=4, arrow_right=False)
for i in range(3):
    box(ax, f(4 * i), 28, f(4 * i + 4) - f(4 * i), 8, 'sujet', label=r'$x$')
brace(ax, f(0), f(12), 38, 'fixe', label=r'$b=12$', down=False)
text(ax, 44, 8, r'$x=b/a=12/3=4$', 'resultat', 'l')
text(ax, 44, 52, r'$a=3$ parts, $a\neq0$', 'varie', 'm')
save(fig, '16-072')
