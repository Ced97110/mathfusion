import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
for cx, t in [(12, 'message'), (44, 'chiffré'), (76, 'retrouvé')]:
    text(ax, cx, 58, t, 'fixe', 's')
for y, (m, c) in [(36, (8, 17)), (12, (22, 33))]:
    box(ax, 3, y, 18, 12, 'sujet', label=str(m))
    box(ax, 35, y, 18, 12, 'fixe', label=str(c))
    box(ax, 67, y, 18, 12, 'resultat', label=str(m))
    arrow(ax, (21.5, y + 6), (34.5, y + 6), 'fixe')
    arrow(ax, (53.5, y + 6), (66.5, y + 6), 'varie')
    text(ax, 28, y + 9.5, r'$m^3$', 'fixe', 's')
    text(ax, 60, y + 9.5, r'$c^{27}$', 'varie', 's')
text(ax, 44, 3, 'reste par 55 à chaque étape', 'encre', 's')
save(fig, '53-096')
