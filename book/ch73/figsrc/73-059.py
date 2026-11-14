import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 58, r'$SL_2$ sur 3 éléments : 24 matrices', 'sujet', 's')
for r in range(2):
    for i in range(6):
        x = 3 + 14*i; y = 34 - 14*r
        box(ax, x, y, 12, 8, 'resultat')
        disc(ax, x+3.5, y+4, 1.5, 'sujet'); disc(ax, x+8.5, y+4, 1.5, 'sujet')
text(ax, 44, 48, 'une classe = a et −a', 'resultat', 's')
brace(ax, 3, 85, 14, 'resultat', r'12 classes : $PSL_2$', size='s')
save(fig, '73-059')
