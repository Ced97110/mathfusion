import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
NB = ' '
fig, ax = canvas(78)
arrow(ax, (82, 68), (8, 68), 'varie')
text(ax, 45, 73, 'lu de droite à gauche', 'varie', 's')
digits = ['4', '3', '2', '9']
mults = ['× 1' + NB + '000', '× 100', '× 10', '× 1']
results = ['4' + NB + '000', '300', '20', '9']
for i in range(4):
    x0 = 6 + 20 * i
    xc = 15 + 20 * i
    box(ax, x0, 50, 18, 12, 'sujet', label=digits[i], size='l', weight='bold')
    text(ax, xc, 43, mults[i], 'fixe', 'm')
    arrow(ax, (xc, 40), (xc, 33), 'varie')
    box(ax, x0, 22, 18, 10, 'resultat', label=results[i], size='m')
brace(ax, 6, 84, 19, 'resultat')
text(ax, 45, 10, '9 + 20 + 300 + 4' + NB + '000 = 4' + NB + '329', 'resultat', 'm', weight='bold')
save(fig, '01-073')
