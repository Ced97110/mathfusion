import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 54, r'$n=1$, $q=3$ : dimension $2n+1=3$', 'encre', 's')
spec = [('facteur', r'$2$', 'autre', r'$2$'), ('puissance', r'$q^{n^2}$', 'sujet', r'$3^1=3$'), ('parenthèse', r'$q^2-1$', 'varie', r'$3^2-1=8$')]
for k, (cap, f, role, val) in enumerate(spec):
    x = 4 + 22 * k
    text(ax, x + 9, 45, cap, role, 's')
    box(ax, x, 28, 18, 12, role, label=f, size='l')
    text(ax, x + 9, 22, val, role, 's')
    if k < 2: text(ax, x + 20, 34, r'$\times$', 'encre', 'l')
arrow(ax, (66, 34), (70, 34), 'varie')
box(ax, 71, 27, 14, 14, 'resultat', label='48', size='l', weight='bold')
text(ax, 78, 22, r'$2\times3\times8$', 'resultat', 's')
text(ax, 33, 10, 'de gauche à droite', 'fixe', 's')
save(fig, '75-136')
