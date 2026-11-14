import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
# le signe radical découpé : indice m, nombre a
text(ax, 24, 90, r'$\sqrt[m]{a}$', 'encre', 30)
text(ax, 62, 97, 'm : l’indice, un entier', 'varie', 's')
text(ax, 62, 90, 'a : un nombre du corps K', 'sujet', 's')
text(ax, 62, 83, 'racine m-ième de a', 'encre', 's')
line(ax, [(2, 76), (86, 76)], 'fixe', dash=True)
# tour pour x^3 - 2 : chaque étage ajoute un radical
text(ax, 22, 69, r'tour de $x^3-2$', 'encre', 's')
box(ax, 2, 46, 40, 14, 'resultat', label=r'$\mathbb{Q}(\sqrt[3]{2},\,j)$', size='s')
box(ax, 2, 26, 40, 10, 'sujet', label=r'$\mathbb{Q}(\sqrt[3]{2})$', size='s')
box(ax, 2, 6, 40, 10, 'fixe', label='ℚ', size='s')
arrow(ax, (22, 36), (22, 46), 'varie', lw=1.2)
arrow(ax, (22, 16), (22, 26), 'varie', lw=1.2)
text(ax, 46, 41, r'ajouter $j$ : $j^3=1$', 'varie', 's', ha='left')
text(ax, 46, 21, r'ajouter $\sqrt[3]{2}$ :', 'varie', 's', ha='left')
text(ax, 46, 16.5, r'$m=3$, $a=2$', 'varie', 's', ha='left')
save(fig, '62-158')
