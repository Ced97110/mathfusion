import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
steps = ['1  choisir l’inconnue', '2  traduire', '3  résoudre', '4  vérifier', '5  conclure']
for i, s in enumerate(steps):
    y = 52 - i * 12
    role = 'resultat' if i == 4 else 'sujet'
    box(ax, 4, y, 40, 8, role, label=s, size='s')
    if i < 4: arrow(ax, (24, y), (24, y - 4), 'varie')
arrow(ax, (44, 8), (49, 8), 'resultat')
box(ax, 49, 3, 36, 10, 'resultat', label='La largeur est 3 m,\nla longueur est 7 m', size='s')
text(ax, 67, 17, 'on s’arrête ici', 'resultat', 's')
save(fig, '16-105')
