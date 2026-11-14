import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 4, 78, 'n² + n + 41 est premier pour :', 'resultat', 's', ha='left')
for n in range(40):
    r, c = divmod(n, 10)
    box(ax, 4 + c * 8.2, 60 - r * 8.2, 7.2, 7.2, 'resultat', r=0.5)
text(ax, 4 + 0, 62.5 + 17, '', 'fixe')
brace(ax, 4, 85.5, 33, 'resultat', label='40 réussites : n de 0 à 39')
box(ax, 4, 3, 80, 21, 'limite')
text(ax, 44, 19, 'n = 40', 'limite', 'm', weight='bold')
text(ax, 44, 12.5, '1600 + 40 + 41 = 1681', 'limite', 's')
text(ax, 44, 7.5, '= 41 × 41 : pas premier', 'limite', 's')
save(fig, '42-086')
