import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 50, '« n est plus petit que 5 »', 'sujet', 'm')
f = numberline(ax, 8, 71, 14, 0, 7, 1)
for k in range(8):
    disc(ax, f(k), 21, 2.4, 'resultat' if k <= 4 else 'limite')
for k in range(4):
    arrow(ax, (f(k), 24.5), (f(k+1), 24.5), 'varie', curve=-0.6)
arrow(ax, (f(4), 24.5), (f(5), 24.5), 'limite', curve=-0.6)
text(ax, 14, 42, 'départ : vrai', 'resultat', 's')
text(ax, 24, 34, 'passage vrai de 0 à 4', 'varie', 's')
text(ax, 64, 34, '4 → 5 : passage faux', 'limite', 's')
text(ax, 62, 42, "5 n'est pas plus petit que 5", 'limite', 's')
save(fig, '01-130')
