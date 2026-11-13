import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# nested sets: the constant 7 sits in R, which sits inside R[e_1, ..., e_r]
box(ax, 3, 6, 82, 52, 'autre', label=None, lw=1.0)
text(ax, 44, 62, r'$R[e_1,\ldots,e_r]$ : polynômes symétriques', 'autre', 's')
box(ax, 8, 11, 40, 38, 'sujet', label=None, lw=1.0)
text(ax, 28, 44, r'$R$ : les constantes', 'sujet', 's')
box(ax, 18, 17, 20, 15, 'resultat', label='7', size='xl', weight='bold')
text(ax, 28, 13.5, 'degré 0', 'fixe', 's')
text(ax, 67, 44, r'$e_1,\ \ldots,\ e_r$', 'fixe', 'm')
text(ax, 67, 36, 'aucun utilisé', 'varie', 's')
text(ax, 67, 29, 'pour écrire 7', 'varie', 's')
save(fig, '55-134')
