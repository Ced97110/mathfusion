import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# proof step 1 on the non-zero elements of the field with 5 elements : commutative, so a product of cyclic groups
steps = [('sujet', 'G : 1, 2, 3, 4 (4 éléments)', 'm'), ('varie', r'commutatif : $2\times3 = 3\times2$', 'm'),
         ('autre', 'produit de groupes cycliques', 'm'), ('resultat', r'$n = p_1^{e_1}\cdots p_k^{e_k}$', 'm')]
for k, (role, lab, sz) in enumerate(steps):
    y = 66 - k * 20
    box(ax, 7, y, 74, 12, role, label=lab, size=sz, lw=1.8 if role == 'varie' else 0.8)
    if k < 3: arrow(ax, (44, y - 0.5), (44, y - 7.5), 'fixe')
text(ax, 44, 4, 'étape décisive : la commutativité', 'varie', 's')
save(fig, '67-081')
