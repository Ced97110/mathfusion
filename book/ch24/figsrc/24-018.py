import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 4, 52, 42, 12, 'fixe', label=r'$ax + by$', size='l')
text(ax, 52, 58, '=', 'encre', 'l')
box(ax, 58, 52, 14, 12, 'sujet', label=r'$c$', size='l')
brace(ax, 6, 44, 51, 'fixe', label='la commande', size='s')
brace(ax, 59, 71, 51, 'sujet', label='le total', size='s')
U = 6.0
for day, c, y in (('Lundi', 5, 26), ('Mardi', 8, 10)):
    text(ax, 2, y, day, 'encre', 'm', ha='left')
    box(ax, 22, y - 4, c * U, 8, 'sujet')
    text(ax, 22 + c * U + 6, y, r'$c = %d$' % c, 'sujet', 'm')
save(fig, '24-018')
