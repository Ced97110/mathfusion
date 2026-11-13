import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
rows = [(46, 'degré 2', 'formule avec une racine', 'resultat'), (26, 'degré 5', 'aucune formule avec radicaux', 'limite'), (6, 'heptagone régulier', 'pas à la règle et au compas', 'limite')]
for y, a, b, r in rows:
    box(ax, 3, y, 28, 12, 'sujet', label=a, size='s')
    arrow(ax, (32, y + 6), (40, y + 6), 'fixe')
    box(ax, 41, y, 45, 12, r, label=b, size='s')
save(fig, '80-491')
