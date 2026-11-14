import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 70, r'$p=2$, $n=2$ coefficients', 'encre', 'm')
for r in range(2):
    for c in range(2):
        box(ax, 28 + 14 * c, 26 + 12 * r, 14, 12, 'sujet', label='%d%d' % (1 - r, c))
brace(ax, 28, 56, 50, 'varie', label=r'2 choix pour $a_2$', down=False)
text(ax, 20, 38, r'2 choix pour $a_1$', 'varie', 's', rot=90)
arrow(ax, (58, 38), (64, 38), 'resultat')
box(ax, 64, 30, 22, 16, 'resultat', label=r'$2\times2=4$', size='s')
text(ax, 44, 14, 'une liste = un seul élément', 'encre', 's')
text(ax, 44, 7, r'donc $p^n=4$ éléments', 'resultat', 'm')
save(fig, '67-027')
