import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
xs = [38, 52, 66]
text(ax, 15, 54, r'$A$', 'sujet', 'l')
text(ax, 17, 38, 'à retirer : A', 'autre', 's')
for i, x in enumerate(xs):
    box(ax, x - 5.5, 49.5, 11, 9, 'sujet', label=str(i + 1))
    box(ax, x - 5.5, 33.5, 11, 9, 'autre', label=str(i + 1))
    arrow(ax, (x, 43.5), (x, 49), 'varie')
box(ax, 40, 14, 24, 11, 'resultat', fill=False, dash=True, label=r'$\varnothing$', size='l')
text(ax, 17, 19.5, 'rien ne reste', 'resultat', 's')
text(ax, 44, 5, r'$A \setminus A = \varnothing$', 'resultat', 'l')
save(fig, '42-143')
