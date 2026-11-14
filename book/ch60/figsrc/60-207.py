import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
yA, yB = 38, 12
box(ax, 2, yA, 10, 10, 'sujet', label='1', size='m')
text(ax, 15, yA + 5, '×', 'encre', 'l')
box(ax, 19, yA, 16, 10, 'sujet', label='λ − 1', size='s')
text(ax, 39, yA + 5, '×', 'encre', 'l')
box(ax, 43, yA, 16, 10, 'sujet', label='λ − 1', size='s')
box(ax, 60, yA, 16, 10, 'sujet', label='λ − 1', size='s')
text(ax, 7, yA - 4, '0 facteur', 'sujet', 's')
text(ax, 7, yA + 12.5, 'facteurs invariants', 'sujet', 's', ha='left')
text(ax, 27, yA - 4, '1 facteur', 'sujet', 's')
brace(ax, 43, 76, yA - 1, 'sujet', label='2 facteurs', size='s')
text(ax, 8, yB + 5, r'$f=$', 'resultat', 'l', weight='bold')
text(ax, 78, yB + 5, r'$=(\lambda-1)^3$', 'resultat', 'm', weight='bold')
for i in range(3):
    box(ax, 16 + i * 18, yB, 16, 10, 'resultat', label='λ − 1', size='s')
brace(ax, 16, 68, yB - 1, 'resultat', label='0 + 1 + 2 = 3 facteurs', size='s')
save(fig, '60-207')
