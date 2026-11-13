import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, 'commutateur de $a$ et $b$', 'encre', 'l')
labs = [r'$a$', r'$b$', r'$a^{-1}$', r'$b^{-1}$']
roles = ['sujet', 'sujet', 'autre', 'autre']
for i in range(4):
    box(ax, 9 + 18 * i, 40, 16, 10, roles[i], label=labs[i], size='l')
brace(ax, 9, 43, 40, 'sujet', label=r'$ab$ : $a$ puis $b$')
brace(ax, 45, 79, 40, 'autre', label=r'$(ba)^{-1}$ : inverse de $ba$')
text(ax, 44, 25, 'dans le triangle', 'fixe', 's')
box(ax, 3, 8, 24, 11, 'sujet', label='$a$ : ⅓ de tour', size='s')
box(ax, 30, 8, 26, 11, 'sujet', label='$b$ : réflexion', size='s')
arrow(ax, (57, 13.5), (63, 13.5), 'varie')
box(ax, 64, 8, 21, 11, 'resultat', label='⅔ de tour\net pas $e$', size='s')
save(fig, '50-209')
