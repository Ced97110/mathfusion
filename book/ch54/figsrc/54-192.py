import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'on change le signe devant $\sqrt{2}$', 'encre', 's')
for y, a, b, calc in [(42, r'$1+\sqrt{2}$', r'$\sqrt{2}-1$', r'$2-1=1$'),
                      (16, r'$3+2\sqrt{2}$', r'$3-2\sqrt{2}$', r'$9-8=1$')]:
    box(ax, 2, y, 28, 12, 'sujet', label=a)
    text(ax, 34, y + 6, r'$\times$', 'encre', 'l')
    box(ax, 38, y, 28, 12, 'autre', label=b)
    text(ax, 70, y + 6, '=', 'encre', 'l')
    box(ax, 74, y, 12, 12, 'resultat', label='1')
    text(ax, 52, y - 4.5, calc, 'fixe', 's')
save(fig, '54-192')
