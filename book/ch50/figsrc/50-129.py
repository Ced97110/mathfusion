import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
rows = [(r'Groupe de 12 : cherche 4', 'sujet', 62), (r'Quotient de 6 : cherche 2', 'sujet', 36), (r'Plus petit : cherche 1', 'resultat', 10)]
for s, role, y in rows:
    box(ax, 14, y, 60, 14, role, label=s)
for y0 in (62, 36):
    arrow(ax, (22, y0), (22, y0 - 12), 'varie')
    text(ax, 25, y0 - 6, 'descendre', 'varie', 's', ha='left')
    arrow(ax, (66, y0 - 12), (66, y0), 'resultat')
    text(ax, 63, y0 - 6, 'remonter', 'resultat', 's', ha='right')
text(ax, 44, 4, "trouver : l'identité suffit", 'resultat', 's')
save(fig, '50-129')
