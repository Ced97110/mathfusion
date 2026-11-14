import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$\{0\}\subset(2)\subset\mathbb{Z}$', 'encre', 'l')
xs = [4, 34, 64]
names = [('sujet', r'$\{0\}$', 'idéal nul'), ('autre', r'$(2)$', 'multiples de 2'), ('fixe', r'$\mathbb{Z}$', 'anneau entier')]
for x, (r, l, cap) in zip(xs, names):
    box(ax, x, 30, 20, 12, r, label=l, size='l')
    text(ax, x + 10, 46, cap, r, 's')
for a, b in [(24, 34), (54, 64)]:
    arrow(ax, (a + 0.5, 36), (b - 0.5, 36), 'fixe')
text(ax, 23, 21, r'$\{0\}$ est premier :', 'resultat', 's')
text(ax, 23, 16, r'$ab=0$ force $a=0$ ou $b=0$', 'resultat', 's')
text(ax, 66, 21, r'pas maximal :', 'limite', 's')
text(ax, 66, 16, r'$(2)$ est entre $\{0\}$ et $\mathbb{Z}$', 'limite', 's')
text(ax, 44, 6, 'premier, mais pas maximal', 'encre', 's')
save(fig, '52-129')
