import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
rows = [(r'$\nu$', 'le nom de l’application', 'sujet'), (r'$R\rightarrow R/I$', 'de l’anneau vers son quotient', 'autre'), (r'$a\mapsto a+I$', 'chaque élément va sur sa classe', 'varie')]
for i, (s, m, r) in enumerate(rows):
    y = 52 - i * 20
    box(ax, 3, y - 7, 28, 14, r, label=s, size='l')
    arrow(ax, (32, y), (38, y), r)
    text(ax, 40, y, m, r, 's', ha='left')
text(ax, 44, 8, r'$\nu(a)$ : la classe de $a$', 'resultat', 's')
save(fig, '52-142')
