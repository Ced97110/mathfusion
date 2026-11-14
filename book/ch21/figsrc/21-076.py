import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def bar(x, y, n, k, role, wd=30):
    for i in range(n): box(ax, x + i * wd / n, y, wd / n, 7, role if i < k else 'fixe', fill=i < k, r=0.2, lw=0.5)
for y, n, k, role, a, b in [(44, 6, 1, 'sujet', r'$\frac{1}{6}$', r'$\frac{2}{12}$'), (14, 4, 1, 'autre', r'$\frac{1}{4}$', r'$\frac{3}{12}$')]:
    bar(4, y, n, k, role); bar(54, y, 12, k * 12 // n, 'resultat')
    text(ax, 19, y + 12, a, role); text(ax, 69, y + 12, b, 'resultat'); text(ax, 44, y + 3.5, r'$=$', 'encre', 'l')
save(fig, '21-076')
