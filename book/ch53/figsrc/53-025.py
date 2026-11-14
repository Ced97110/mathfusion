import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'le chiffrement = la règle', 'sujet', 'l', weight='bold')
# la règle (au centre) : une seule, pour tous les mots
box(ax, 32, 14, 24, 34, 'sujet', label=None)
text(ax, 44, 38, 'règle', 'sujet', 'l')
text(ax, 44, 30, 'ajouter 3', 'sujet', 'm')
text(ax, 44, 22, 'à chaque numéro', 'sujet', 's')
# deux mots clairs, deux mots chiffrés
rows = [(40, 'ALGEBRE', 'DOJHEUH', 'fixe', 'resultat'), (14, 'un autre mot', 'son chiffré', 'fixe', 'resultat')]
for y, a, b, r1, r2 in rows:
    box(ax, 2, y, 24, 8, r1, label=a)
    box(ax, 62, y, 24, 8, r2, label=b)
    arrow(ax, (26, y + 4), (32, y + 4 + (-4 if y > 30 else 4) * 0.0), 'varie')
    arrow(ax, (56, y + 4), (62, y + 4), 'varie')
text(ax, 14, 52, 'le premier jour', 'fixe', 's')
text(ax, 14, 8, 'le lendemain', 'fixe', 's')
save(fig, '53-025')
