import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 70, r'$\alpha^2$ est l’un des quatre :', 'encre', 'm')
labs = ['0', r'$\alpha$', '1', r'$\alpha+1$']
why = [r'$\alpha\times\alpha=0$', r'$\alpha(\alpha+1)=0$', r'$(\alpha+1)^2=0$']
for i in range(4):
    x = 4 + 21 * i
    box(ax, x, 48, 19, 12, 'resultat' if i == 3 else 'limite', label=labs[i], size='l')
    if i < 3: text(ax, x + 9.5, 41, why[i], 'limite', 's')
brace(ax, 4, 62, 37, 'limite', label='produit nul : impossible')
text(ax, 76.5, 41, 'seul cas\npossible', 'resultat', 's')
text(ax, 44, 8, r'donc $\alpha^2=\alpha+1$', 'resultat', 'l')
save(fig, '67-014')
