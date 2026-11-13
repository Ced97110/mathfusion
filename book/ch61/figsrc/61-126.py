import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 22, 61, 'théorème 2', 'autre', 'm', weight='bold'); text(ax, 66, 61, 'théorème $C$', 'sujet', 'm', weight='bold')
box(ax, 4, 42, 36, 10, 'autre', label='degré 2', size='m'); box(ax, 4, 26, 36, 10, 'autre', label='degré 2', size='m')
text(ax, 22, 13, r'$2 \times 2 = 4$', 'resultat', 'l')
box(ax, 48, 42, 36, 10, 'sujet', label=r'degré $\infty$', size='m'); box(ax, 48, 26, 36, 10, 'sujet', label=r'degré $\infty$', size='m')
text(ax, 66, 13, 'pas de produit', 'limite', 'm')
text(ax, 44, 5, 'des degrés finis', 'autre', 's', ha='right') if False else None
save(fig, '61-126')
