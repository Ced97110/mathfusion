import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# x^2 - 5x + 6 = (x-2)(x-3) : r1 + r2 = 5 = -a, so r2 = 5 - r1
text(ax, 44, 62, r'$x^2-5x+6=(x-2)(x-3)$', 'encre', 'm')
x0, x1 = 8, 72
g = numberline(ax, x0, x1, 28, 0, 6, 1, labels=True, arrow_right=False, every=1)
box(ax, g(0), 34, g(2) - g(0), 9, 'sujet', label=r'$r_1=2$')
box(ax, g(2), 34, g(5) - g(2), 9, 'resultat', label=r'$r_2=3$')
brace(ax, g(0), g(5), 46, 'varie', label=r'$r_1+r_2=5=-a$', down=False)
arrow(ax, (g(5), 31.5), (g(2), 31.5), 'varie', curve=0.0, both=False)
text(ax, 44, 8, r'$r_2=5-r_1=5-2=3$', 'resultat', 'm')
save(fig, '62-119')
