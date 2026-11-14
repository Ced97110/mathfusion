import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
# deux espaces, deux bases de 2 vecteurs : même nombre, deux noms
def panel(x, role, title, tag):
    box(ax, x, 16, 30, 36, role)
    text(ax, x + 15, 46, title, role, 's')
    for i in range(2):
        box(ax, x + 3.5 + i * 12.5, 26, 11, 10, role, label=['(1, 0)', '(0, 1)'][i], size='s', r=0.4, fill=False)
    line(ax, [(x + 15, 16), (x + 15, 12)], 'varie')
    box(ax, x + 3, 3, 24, 9, 'varie', label=tag, size='m')
panel(2, 'sujet', 'couples d’entiers', 'rang')
panel(56, 'autre', 'plan réel', 'dimension')
arrow(ax, (32, 34), (38, 34), 'resultat')
arrow(ax, (56, 34), (50, 34), 'resultat')
box(ax, 38, 28, 12, 12, 'resultat', label='2', size='l', weight='bold')
text(ax, 44, 22, 'même nombre', 'resultat', 's')
save(fig, '58-182')
