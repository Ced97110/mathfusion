import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
c = 4.6
for b in range(2):
    for r in range(3):
        for k in range(8):
            box(ax, 6 + c * k, 50 - (b * 3 + r) * c - b * 3 - c, c, c, 'sujet', lw=0.5, r=0.3)
brace(ax, 6, 6 + 8 * c, 50 - 6 * c - 3 - 1, 'fixe', label='8 colonnes')
text(ax, 24, 6, '2 blocs de 3 lignes', 'fixe', 's')
text(ax, 65, 40, '48', 'sujet', 'xl', weight='bold'); text(ax, 65, 32, r'$=2\times3\times8$', 'sujet', 's')
text(ax, 65, 22, 'le nombre,', 'limite', 's'); text(ax, 65, 17, 'pas la liste', 'limite', 's')
save(fig, '75-137')
