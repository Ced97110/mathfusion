import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 36, 76, r'sans $\sqrt{-3}$', 'fixe', 's')
text(ax, 71, 76, r'coeff. de $\sqrt{-3}$', 'varie', 's')
rows = [(58, r'$1$', 'fixe', r'$1$', r'$0$'),
        (43, r'$w$', 'sujet', r'$-\frac{1}{2}$', r'$+\frac{1}{2}$'),
        (28, r'$w^2$', 'autre', r'$-\frac{1}{2}$', r'$-\frac{1}{2}$')]
for y, lab, role, a, b in rows:
    text(ax, 9, y, lab, role, 'm')
    box(ax, 20, y - 5.5, 32, 11, role, label=a)
    box(ax, 56, y - 5.5, 30, 11, role, label=b)
line(ax, [(3, 20), (86, 20)], 'fixe')
text(ax, 9, 10, 'somme', 'resultat', 's')
box(ax, 20, 4.5, 32, 11, 'resultat', label=r'$0$')
box(ax, 56, 4.5, 30, 11, 'resultat', label=r'$0$')
save(fig, '65-156')
