import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 2, 57, "ensembles (ch. 43)", 'fixe', 's', ha='left')
text(ax, 2, 29, "groupes (ch. 48)", 'sujet', 's', ha='left')
tops = [(4, r"$S$"), (34, r"$S/\!\sim$"), (68, r"$G'$")]
for x, l in tops: box(ax, x, 40, 18, 11, 'fixe', label=l, size='s')
arrow(ax, (22, 45.5), (34, 45.5), 'fixe'); arrow(ax, (52, 45.5), (68, 45.5), 'fixe')
text(ax, 28, 50, "regroupe", 'fixe', 's'); text(ax, 60, 50, "injective", 'fixe', 's')
bots = [(4, r"$G$"), (34, r"$G/K$"), (68, r"$G'$")]
for x, l in bots: box(ax, x, 10, 18, 11, 'sujet', label=l, size='s')
arrow(ax, (22, 15.5), (34, 15.5), 'varie'); arrow(ax, (52, 15.5), (68, 15.5), 'resultat')
text(ax, 28, 11.5-0.0+7, r"$\nu$", 'varie', 'm'); text(ax, 60, 11.5+7, r"$\bar f$", 'resultat', 'm')
arrow(ax, (43, 40), (43, 21), 'varie', both=True)
text(ax, 46, 33, r"classes de $K$ : l'opération", 'varie', 's', ha='left')
text(ax, 44, 3, r"$\bar f$ respecte le produit", 'resultat', 's')
save(fig, '48-073')
