import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 3, 48, 22, 11, 'sujet', label=r'$d = rt$', size='l')
arrow(ax, (26, 53.5), (57, 53.5), 'varie')
text(ax, 41.5, 57, r'divise par $r$', 'varie', 's')
box(ax, 60, 48, 25, 11, 'resultat', label=r'$t = d\,/\,r$', size='l')
for i in range(3):
    box(ax, 8 + i * 24, 22, 24, 10, 'sujet', label='50 km', size='s')
brace(ax, 8, 80, 21, 'sujet', label='150 km', depth=1.8)
text(ax, 44, 40, r'$t$ = 150 ÷ 50 = 3 h', 'resultat', 'm', weight='bold')
text(ax, 44, 5, 'vérifie : 50 × 3 = 150', 'resultat', 's')
save(fig, '16-119')
