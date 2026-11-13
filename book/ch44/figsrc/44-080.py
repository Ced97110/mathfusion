import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
x0, y = 18, 28
xs = [x0 + i * 10 for i in range(2)] + [x0 + 26 + i * 10 for i in range(3)]
for x in xs: box(ax, x, y, 8, 8, 'sujet', label=r'$\alpha$')
brace(ax, xs[0], xs[1] + 8, y + 9, 'sujet', r'$k=2$', down=False)
brace(ax, xs[2], xs[4] + 8, y + 9, 'sujet', r'$l=3$', down=False)
brace(ax, xs[0], xs[4] + 8, y - 1, 'resultat', r'$k+l=5$ facteurs', down=True)
text(ax, 44, 8, r'$\alpha^{k}\circ\alpha^{l}=\alpha^{k+l}$', 'encre', 'l')
save(fig, '44-080')
