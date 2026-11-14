import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 44, 82, r'$a=1$ : $1+x$', 'encre', 'l')
for k in range(4):
    y = 60 - k * 17
    box(ax, 6, y, 22, 11, 'sujet', label=str(k)); arrow(ax, (30, y + 5.5), (44, y + 5.5), 'varie')
    text(ax, 37, y + 9.5, '1 +', 'varie', 's')
    box(ax, 46, y, 22, 11, 'resultat' if k < 3 else 'varie', label=str(k + 1))
text(ax, 77, 11.5, 'reste 0', 'varie', 's')
text(ax, 77, 28.5, '', 'fixe', 's')
save(fig, '45-078')
