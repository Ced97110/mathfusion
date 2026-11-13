import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for k in (0, 1):
    pass
line(ax, [(6, 48), (24, 48)], 'sujet'); line(ax, [(36, 48), (52, 48)], 'sujet'); line(ax, [(64, 48), (82, 48)], 'sujet')
box(ax, 24, 44.5, 12, 7, 'sujet', label=r'$A$'); box(ax, 52, 44.5, 12, 7, 'sujet', label=r'$B$')
text(ax, 44, 61, r'série : $A \cap B$', 'sujet', 'm'); text(ax, 44, 56, 'passe si A et B fermés', 'sujet', 's')
for y in (26, 13): pass
line(ax, [(10, 26), (38, 26)], 'autre'); line(ax, [(50, 26), (78, 26)], 'autre')
line(ax, [(10, 13), (38, 13)], 'autre'); line(ax, [(50, 13), (78, 13)], 'autre')
line(ax, [(10, 13), (10, 26)], 'autre'); line(ax, [(78, 13), (78, 26)], 'autre')
line(ax, [(4, 19.5), (10, 19.5)], 'autre'); line(ax, [(78, 19.5), (84, 19.5)], 'autre')
box(ax, 38, 22.5, 12, 7, 'autre', label=r'$A$'); box(ax, 38, 9.5, 12, 7, 'autre', label=r'$B$')
text(ax, 44, 40, r'parallèle : $A \cup B$', 'autre', 'm'); text(ax, 44, 35, 'passe si A ou B fermé', 'autre', 's')
text(ax, 44, 3, "fermé = dans l'ensemble", 'fixe', 's')
save(fig, '42-307')
