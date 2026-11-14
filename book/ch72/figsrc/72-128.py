import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 66, 'même espace, deux découpages', 'fixe', 's')
for y, r, lab in ((42, 'sujet', r'$H$ hyperbolique'), (14, 'autre', r"$H'$ hyperbolique")):
    box(ax, 4, y, 40, 12, r, label=lab, size='s'); text(ax, 48, y + 6, r'$\perp$', 'encre', 'm')
    box(ax, 52, y, 24, 12, 'fixe', label=r'$X$' if y == 42 else r"$X'$")
arrow(ax, (64, 42), (64, 26), 'resultat', both=True); text(ax, 67, 34, 'isométriques', 'resultat', 's', ha='left')
text(ax, 44, 5, r'$X$ unique à isométrie près', 'resultat', 'm', weight='bold')
save(fig, '72-128')
