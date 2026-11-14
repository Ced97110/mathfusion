import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
x = [4, 27, 50]; lab = [r'$\sigma$', r"$\sigma'$"]
for i in range(3): box(ax, x[i], 54, 20, 8, 'sujet' if i == 0 else 'autre', label='échange')
brace(ax, 4, 24, 64, 'sujet', r'$\sigma=(1\ 2)$', down=False)
brace(ax, 27, 70, 64, 'autre', r"$\sigma'=(1\ 2\ 3)$", down=False)
brace(ax, 4, 70, 54, 'varie', '1 + 2 = 3 échanges', down=True)
text(ax, 44, 26, 'signature du produit :', 'encre', 'm')
box(ax, 8, 8, 72, 11, 'resultat', label=r'$-1 = (-1)\times(+1)$', size='l')
save(fig, '46-226')
