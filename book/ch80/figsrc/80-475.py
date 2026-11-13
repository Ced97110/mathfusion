import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(60)
box(ax, 3, 1, 82, 47, 'fixe', fill=False, dash=True, r=2.0)
text(ax, 44, 53, 'classe : même table', 'encre', 'm')
box(ax, 8, 12, 40, 30, 'sujet')
for i in range(6):
    box(ax, 12 + (i % 3) * 11, 28 - (i // 3) * 10 + 2 - 2, 8, 7, 'sujet', fill=False, lw=0.7)
text(ax, 28, 16, r'$C$ : 6 interrupteurs', 'sujet', 's')
box(ax, 54, 12, 27, 30, 'resultat', lw=2.0)
box(ax, 63, 28, 9, 7, 'resultat', fill=False, lw=0.7)
text(ax, 67.5, 20, r'$a$ : 1', 'resultat', 's'); text(ax, 67.5, 16, 'choisi', 'resultat', 's')
text(ax, 44, 6.5, r'on garde le plus petit : $1<6$', 'resultat', 's', weight='bold')
save(fig, '80-475')
