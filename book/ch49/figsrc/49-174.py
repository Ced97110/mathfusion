import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
disc(ax, 16, 40, 6, 'sujet', label=r'$s$', size='l'); disc(ax, 72, 40, 6, 'resultat', label=r"$s'$", size='l')
arrow(ax, (22, 46), (66, 46), 'varie', curve=-0.3); text(ax, 44, 58, r"$s' = r\,s\,r^{-1}$", 'varie', 'm')
arrow(ax, (66, 34), (22, 34), 'autre', curve=-0.3); text(ax, 44, 21, r"$s = r^{-1}s'\,r$", 'autre', 'm')
text(ax, 44, 8, "chaque geste annule l'autre", 'resultat', 's')
save(fig, '49-174')
