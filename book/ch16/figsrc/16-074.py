import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 10, 76, 18, 0, 12, every=3, arrow_right=False)
for i in range(4):
    box(ax, f(3 * i), 28, f(3 * i + 3) - f(3 * i), 8, 'fixe', label='3')
brace(ax, f(0), f(12), 38, 'sujet', label=r'$x$', down=False)
text(ax, 44, 8, r'$x=4\times3=12$', 'resultat', 'l')
text(ax, 44, 50, r'$x/4=3$ : 4 parts de 3', 'varie', 'm')
save(fig, '16-074')
