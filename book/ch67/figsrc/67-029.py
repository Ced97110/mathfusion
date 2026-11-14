import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 86, r'$F$ a $q=4$ éléments', 'autre', 'm')
text(ax, 44, 79, r'$[E:F]=n=2$', 'autre', 'm')
for i in range(4):
    for j in range(4):
        disc(ax, 30 + 8 * j, 30 + 8 * i, 2.8, 'sujet')
brace(ax, 27, 57, 57, 'varie', label=r'$a_2$ : 4 valeurs', down=False)
text(ax, 17, 42, r'$a_1$ : 4 valeurs', 'varie', 's', rot=90)
arrow(ax, (60, 42), (65, 42), 'resultat')
box(ax, 65, 34, 21, 16, 'resultat', label=r'$4\times4=16$', size='s')
text(ax, 44, 17, r'chaque point : un élément de $E$', 'sujet', 's')
text(ax, 44, 8, r'$E$ a $q^n=4^2$ éléments', 'resultat', 'm')
save(fig, '67-029')
