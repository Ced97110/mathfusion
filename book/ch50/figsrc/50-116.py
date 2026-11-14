import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# |G| = 2 x 3 : the whole share of p is the factor 2
text(ax, 10, 72, r'$|G|=6=$', 'encre', 'm')
box(ax, 28, 67, 12, 10, 'sujet', label='2', size='l'); text(ax, 45, 72, r'$\times$', 'encre', 'm')
box(ax, 50, 67, 12, 10, 'fixe', label='3', size='l')
text(ax, 34, 63, 'part de $p$', 'sujet', 's'); text(ax, 56, 63, 'reste', 'fixe', 's')
# G cut in k blocks, each as large as N(P)
X0, BW, G = 14, 18, 6
for i in range(3):
    x = X0 + i * (BW + G)
    box(ax, x, 36, BW, 12, 'sujet' if i == 0 else 'fixe')
    for j in range(2): disc(ax, x + 5 + 8 * j, 42, 2.6, 'sujet' if i == 0 else 'fixe')
text(ax, X0 + BW / 2, 52, r'$N(P)$ : 2', 'sujet', 's')
brace(ax, X0, X0 + 3 * BW + 2 * G, 34, 'fixe', label=r'$k=3$ blocs', down=True)
text(ax, 44, 17, r'$k = 6\,/\,2 = 3$ : sans facteur 2', 'resultat', 's')
text(ax, 44, 9, r'$2$ ne divise pas $3$', 'resultat', 'm')
save(fig, '50-116')
