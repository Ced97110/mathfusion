import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(80)
# le nombre géant, jamais écrit
box(ax, 2, 64, 84, 10, 'fixe', fill=False, dash=True)
text(ax, 26, 69, r'$17^{27}$ a 34 chiffres', 'fixe', 'm')
text(ax, 68, 69, 'jamais écrit', 'fixe', 'm')
# 4 carrés : cinq lignes, toutes inférieures à 55
vals = ['17', '14', '31', '26', '16']
for i, v in enumerate(vals):
    box(ax, 2 + 18 * i, 40, 12, 10, 'fixe' if v == '31' else 'resultat', label=v)
    if i < 4:
        arrow(ax, (14.5 + 18 * i, 45), (19.5 + 18 * i, 45), 'varie')
brace(ax, 2, 86, 40, 'varie', label='4 carrés, puis reste par 55')
# 3 produits des lignes vertes
arrow(ax, (44, 31), (44, 21.5), 'varie')
text(ax, 48, 26, '3 produits, reste par 55', 'varie', 's', ha='left')
box(ax, 28, 11, 32, 10, 'sujet', label=r'$17^{27}\equiv 8$')
text(ax, 73, 16, 'plus grand\nnombre écrit :\n961', 'fixe', 's')
save(fig, '53-131')
