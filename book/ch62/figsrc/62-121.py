import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# no integer cube equals 2 ; so x^3 - 2 is irreducible ; K = Q(r1) has the base 1, r1, r1^2
text(ax, 44, 68, r'un cube entier vaut-il $2$ ?', 'encre', 'm')
y = 50
g = numberline(ax, 6, 76, y, 0, 9, 1, labels=False, arrow_right=False)
disc(ax, g(1), y, 1.8, 'fixe'); text(ax, g(1), y - 5.5, r'$1^3=1$', 'fixe', 's')
disc(ax, g(8), y, 1.8, 'fixe'); text(ax, g(8), y - 5.5, r'$2^3=8$', 'fixe', 's')
disc(ax, g(2), y, 1.8, 'varie'); text(ax, g(2), y + 5.5, r'$2$', 'varie', 'm')
text(ax, 44, 40, 'aucun cube entier ne vaut 2', 'varie', 's')
text(ax, 44, 33, r'donc $x^3-2$ est irréductible', 'encre', 's')
for i, lab in enumerate((r'$1$', r'$r_1$', r'$r_1^2$')):
    box(ax, 12 + i * 22, 6, 20, 12, 'sujet', label=lab)
brace(ax, 12, 76, 20, 'sujet', label='base de $K$ : degré 3', down=False)
save(fig, '62-121')
