import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
text(ax, 44, 42, r'$\frac{1}{2}+\frac{1}{3}$ ne vaut pas $\frac{2}{5}$', 'encre', 'm')
f = numberline(ax, 6, 76, 22, 0, 1, 0.5)
for v, r, s, dy in [(0.4, 'limite', r'$\frac{2}{5}$ (faux)', -11), (0.5, 'sujet', r'$\frac{1}{2}$', 8), (5 / 6, 'resultat', r'$\frac{5}{6}$ (vrai)', 8)]:
    disc(ax, f(v), 22, 1.4, r)
    text(ax, f(v), 22 + dy, s, r, 's')
save(fig, '21-079')
