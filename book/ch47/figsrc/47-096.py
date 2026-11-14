import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
f = numberline(ax, 4, 76, 40, 0, 30, step=3, every=1)
for v in (3, 15, 27):
    disc(ax, f(v), 40, 2.0, 'sujet')
arrow(ax, (f(3), 43), (f(15), 43), 'varie', curve=-0.45); arrow(ax, (f(15), 43), (f(27), 43), 'varie', curve=-0.45)
text(ax, f(9), 55, '+ 12', 'varie', 's'); text(ax, f(21), 55, '+ 12', 'varie', 's')
text(ax, 44, 62, 'même heure sur l’horloge à 12 heures', 'fixe', 's')
text(ax, 44, 22, r'$27\equiv15\equiv3\ (\mathrm{mod}\ 12)$', 'resultat', 'l')
text(ax, 24, 11, r'$\equiv$ : est congru à', 'sujet', 's')
text(ax, 66, 11, r'$12$ : l’horloge', 'varie', 's')
save(fig, '47-096')
