import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 54, r'$P(2)\times P(3)\times P(1)$', 'sujet', 'm')
text(ax, 44, 45, r'$2\times3\times1=6$', 'resultat', 'l', weight='bold')
for i in range(6):
    box(ax, 2 + 11.5 * i, 24, 10, 10, 'resultat', label=str(i + 1))
box(ax, 2 + 11.5 * 6, 24, 10, 10, 'limite', label='7', dash=True)
brace(ax, 2, 2 + 11.5 * 5 + 10, 24, 'resultat', label='six groupes')
text(ax, 76, 15, 'pas de 7e', 'limite', 's')
save(fig, '60-238')
