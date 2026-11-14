import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
box(ax, 2, 68, 84, 10, 'limite', label=r'$|C|=1$ : exclu', size='m')
box(ax, 2, 4, 84, 10, 'resultat', label=r'$|C|=9$ : tout commute', size='m')
text(ax, 44, 60, r'$|C|=3$ : étape décisive', 'varie', 'm')
labs = [r'$C$', r'$aC$', r'$a^2C$']
for x, l in zip([6, 33, 60], labs):
    box(ax, x, 38, 22, 15, 'sujet')
    for i in range(3):
        disc(ax, x+5+i*6, 45.5, 2.4, 'sujet')
    text(ax, x+11, 33.5, l, 'sujet', 's')
arrow(ax, (28.5, 45.5), (32.5, 45.5), 'varie')
arrow(ax, (55.5, 45.5), (59.5, 45.5), 'varie')
brace(ax, 6, 82, 29, 'varie', label='3 paquets : G/C cyclique')
arrow(ax, (44, 20), (44, 15), 'resultat')
save(fig, '49-281')
