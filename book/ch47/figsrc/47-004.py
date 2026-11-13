import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 52, 'Groupe de 8 éléments', 'sujet', 'm')
text(ax, 44, 45, 'taille du sous-groupe', 'encre', 's')
ok = {1, 2, 4, 8}
for i in range(8):
    n = i + 1; x = 6 + i * 10; r = 'resultat' if n in ok else 'limite'
    box(ax, x, 27, 8, 11, r, label=str(n), size='l')
text(ax, 22, 20, '1, 2, 4, 8 divisent 8', 'resultat', 's'); text(ax, 66, 20, '3, 5, 6, 7 : non', 'limite', 's')
text(ax, 22, 8, r'$8 = 4 \times 2$', 'resultat', 'm')
text(ax, 66, 8, r'$3\times 2=6$ ; $3\times 3=9$', 'limite', 's')
save(fig, '47-004')
