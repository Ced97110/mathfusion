import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ds = [1, 2, 3, 4, 6, 12]
for i, d in enumerate(ds):
    box(ax, 3 + 13.5 * i, 40, 11, 9, 'sujet' if i == 0 else 'fixe', label=str(d))
text(ax, 8.5, 53, 'premier', 'sujet', 's')
text(ax, 30, 53, 'rien sous 1', 'fixe', 's')
arrow(ax, (8.5, 40), (8.5, 30), 'varie')
box(ax, 4, 14, 30, 14, 'resultat', label=r'$g(1)$')
text(ax, 44, 21, '=', 'encre', 'l')
box(ax, 54, 14, 30, 14, 'sujet', label=r'$f(1)$')
text(ax, 44, 6, '1 seul terme dans le total', 'encre', 's')
save(fig, '80-268')
