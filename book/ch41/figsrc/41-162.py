import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
# 4 règles pour l'addition + 4 règles pour la multiplication par un scalaire = 8
text(ax, 23, 86, 'addition', 'sujet', 'm', weight='bold')
text(ax, 65, 86, 'par un scalaire', 'varie', 'm', weight='bold')
left = ['ordre', 'regroupement', 'vecteur nul', 'opposé']
right = [r'$(ab)\,v$', r'$1\cdot v$', r'$a(u+v)$', r'$(a+b)\,v$']
for i, (l, r) in enumerate(zip(left, right)):
    y = 66 - i * 14
    box(ax, 4, y, 38, 11, 'sujet', label=l, size='s')
    box(ax, 46, y, 38, 11, 'varie', label=r, size='s')
brace(ax, 4, 42, 22, 'sujet', label='4 règles', down=True)
brace(ax, 46, 84, 22, 'varie', label='4 règles', down=True)
box(ax, 14, 2, 60, 10, 'resultat', label='espace vectoriel : 8 règles', size='s')
save(fig, '41-162')
