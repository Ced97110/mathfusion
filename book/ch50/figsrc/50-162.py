import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for (y, n, other, note) in [(44, 3, 5, r'$5-1=4$ : pas multiple de 3'), (18, 5, 3, r'$3-1=2$ : pas multiple de 5')]:
    text(ax, 3, y + 4.5, rf'$n_{n}$ divise {other}', 'encre', 'm', ha='left')
    box(ax, 32, y, 10, 9, 'limite', label=str(other))
    line(ax, [(33, y + 1.5), (41, y + 7.5)], 'limite', lw=1.1)
    box(ax, 45, y, 10, 9, 'resultat', label='1')
    text(ax, 32, y - 4, note, 'limite', 's', ha='left')
    arrow(ax, (57, y + 4.5), (64, y + 4.5), 'resultat')
    box(ax, 64, y, 21, 9, 'resultat', label=rf'$n_{n}=1$')
text(ax, 44, 60, 'même calcul, deux fois', 'encre', 'm')
save(fig, '50-162')
