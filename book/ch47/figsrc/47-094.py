import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 65, r'$A_4$ : 12 éléments', 'sujet', 'm')
text(ax, 66, 65, r'sous-groupe de 6 ?', 'limite', 'm')
for i in range(12):
    box(ax, 4 + (i % 3) * 12, 48 - (i // 3) * 11, 10.5, 9.5, 'sujet', r=0.4, lw=0.6)
for i in range(6):
    box(ax, 48 + (i % 3) * 12, 42 - (i // 3) * 12 + 6, 10.5, 9.5, 'limite', fill=False, dash=True, r=0.4, lw=0.6)
text(ax, 66, 18, 'aucun', 'limite', 'l')
text(ax, 44, 8, r'6 divise 12, mais 6 est impossible', 'limite', 's')
save(fig, '47-094')
