import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ax.add_patch(Circle((44, 34), 31, ec=COL['sujet'], fc=FILL['sujet'], lw=0.9, zorder=1))
text(ax, 44, 69, r'$G_f$ : 6 permutations', 'sujet', 's')
ax.add_patch(Circle((55, 34), 15, ec=COL['autre'], fc=FILL['resultat'], lw=1.0, ls='--', zorder=1.6))
text(ax, 55, 51.5, r'$A_3$ : paires', 'autre', 's')
for j, y in enumerate((44, 34, 24)):
    disc(ax, 28, y, 4.2, 'fixe')
    disc(ax, 55, y, 4.2, 'resultat')
text(ax, 28, 14, 'impaires : 3', 'fixe', 's')
text(ax, 55, 14, r'$G_f\cap A_3$ : 3', 'resultat', 's')
save(fig, '65-032')
