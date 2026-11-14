import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 30, 40, 'ker', 'sujet', 14, weight='bold'); text(ax, 56, 40, r'$\eta$', 'varie', 16)
arrow(ax, (30, 32), (22, 22), 'sujet'); arrow(ax, (56, 32), (64, 22), 'varie')
text(ax, 20, 17, 'un mot :\nkernel = noyau', 'sujet', 's'); text(ax, 66, 17, "l'application\nconsidérée", 'varie', 's')
text(ax, 44, 52, 'noyau de êta', 'fixe', 's')
text(ax, 44, 4, 'ex. : ker $\\eta$ = multiples de 4', 'resultat', 's')
save(fig, '52-146')
