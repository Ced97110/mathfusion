import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
cop = {1, 7, 11, 13, 17, 19, 23, 29}
text(ax, 44, 58, '1 à 30, par lignes de 10', 'fixe', 's')
for n in range(1, 31):
    r, c = divmod(n - 1, 10)
    box(ax, 5 + 8 * c, 42 - 8 * r, 7, 7, 'resultat' if n in cop else 'sujet', r=0.4, lw=0.6)
text(ax, 44, 20, '22 : facteur commun avec 30', 'sujet', 's')
text(ax, 44, 13, r'$15+10+6-5-3-2+1=22$', 'sujet', 's')
text(ax, 44, 6, r'$30-22=8$ : sans facteur', 'resultat', 's')
save(fig, '80-356')
