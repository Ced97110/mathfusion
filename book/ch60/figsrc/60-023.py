import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 16, 62, 'ℤ/12', 'sujet', 'l'); text(ax, 70, 62, 'ℤ/4 ⊕ ℤ/3', 'autre', 'l')
text(ax, 43, 62, '≅', 'resultat', 'xl', weight='bold')
for y, a, b in ((46, '7', '(3, 1)'), (32, '5', '(1, 2)'), (18, '0', '(0, 0)')):
    box(ax, 6, y - 4, 20, 8, 'sujet', label=a, size='m'); box(ax, 52, y - 4, 32, 8, 'autre', label=b, size='m')
    arrow(ax, (27.5, y), (50.5, y), 'varie', both=True)
text(ax, 39, 51, 'renommer', 'varie', 's')
text(ax, 44, 6, 'même rôle dans l’addition', 'encre', 's')
save(fig, '60-023')
