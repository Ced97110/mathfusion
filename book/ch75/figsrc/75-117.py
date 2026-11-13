import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cw = 6.5
text(ax, 2, 74, r'$q=3$ : 48 inversibles', 'encre', 's', ha='left')
for c in range(12):
    for r in range(4):
        box(ax, 5 + c * cw, 52 + r * 4.5 - 0, cw, 4.5, 'resultat' if r < 2 else 'fixe', r=0.3, lw=0.4)
text(ax, 44, 46, '24 de déterminant 1, 24 de déterminant 2', 'encre', 's')
text(ax, 2, 36, r'$q=2$ : 6 inversibles', 'encre', 's', ha='left')
for c in range(6):
    box(ax, 5 + c * 12, 24, 12, 8, 'resultat', r=0.3, lw=0.4, label='1')
text(ax, 44, 18, 'les 6 ont un déterminant 1', 'resultat', 's')
box(ax, 14, 3, 60, 9, 'sujet', label=r'$SL_{n}=GL_{n}$', size='l')
save(fig, '75-117')
