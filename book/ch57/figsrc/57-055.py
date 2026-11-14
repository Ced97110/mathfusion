import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 31, 60, r'$e\mapsto(2\,;\,1)$', 'sujet', 's')
text(ax, 59, 60, r'$f\mapsto(3\,;\,5)$', 'autre', 's')
text(ax, 31, 53, r'$\eta(e)=(a\,;\,b)$', 'sujet', 's')
text(ax, 59, 53, r'$\eta(f)=(c\,;\,d)$', 'autre', 's')
cells = [(20, 28, 'sujet', r'$a=2$'), (20, 12, 'sujet', r'$b=1$'),
         (44, 28, 'autre', r'$c=3$'), (44, 12, 'autre', r'$d=5$')]
for x, y, role, lab in cells:
    box(ax, x, y, 22, 12, role, label=lab, size='m')
line(ax, [(19.2, 9), (17.2, 9), (17.2, 43), (19.2, 43)], 'encre', lw=1.0)
line(ax, [(67.8, 9), (69.8, 9), (69.8, 43), (67.8, 43)], 'encre', lw=1.0)
text(ax, 8, 26, 'matrice', 'encre', 's')
text(ax, 44, 3, 'quatre entiers rangés en deux colonnes', 'fixe', 's')
save(fig, '57-055')
