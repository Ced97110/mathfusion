import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 4, 44, 38, 24, 'sujet'); box(ax, 46, 44, 38, 24, 'autre')
text(ax, 23, 61, r'$e_G$', 'sujet', 'xl'); text(ax, 23, 51, r'$=0$ dans $G$', 'sujet', 's')
text(ax, 65, 61, r'$e_H$', 'autre', 'xl'); text(ax, 65, 51, r'$=0$ dans $H$', 'autre', 's')
arrow(ax, (23, 43), (36, 29), 'sujet'); arrow(ax, (65, 43), (52, 29), 'autre')
box(ax, 20, 13, 48, 15, 'resultat', label=r'$(e_G,\,e_H)=(0,\,0)$', size='m')
text(ax, 44, 6, r'neutre de $G\times H$', 'resultat', 's')
save(fig, '45-159')
