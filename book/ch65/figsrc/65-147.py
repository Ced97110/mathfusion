import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = numberline(ax, 10, 70, 30, 2, 6, step=1)
for d in (2, 3, 4):
    disc(ax, f(d), 30, 2.2, 'resultat')
for d in (5, 6):
    disc(ax, f(d), 30, 2.2, 'limite')
text(ax, 44, 56, 'degré de l\'équation', 'encre', 's')
brace(ax, f(2) - 3, f(4) + 3, 38, 'resultat', label='une formule existe', down=False)
brace(ax, f(5) - 3, f(6) + 3, 38, 'limite', label='aucune formule', down=False)
text(ax, f(2), 12, 'chapitre 23', 'sujet', 's')
text(ax, f(5) + 8, 12, 'chapitre 65', 'limite', 's')
save(fig, '65-147')
