import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 21, 65, 'Dans $\\mathcal{P}(\\mathbb{Z})$', 'fixe', 's', weight='bold')
text(ax, 67, 65, 'Dans les sous-groupes', 'fixe', 's', weight='bold')
for cx in (21, 67):
    box(ax, cx - 18, 4, 16, 11, 'sujet', label='$2\\mathbb{Z}$', size='s')
    box(ax, cx + 2, 4, 16, 11, 'autre', label='$3\\mathbb{Z}$', size='s')
box(ax, 3, 36, 36, 14, 'fixe', label='sup = union\n$2\\mathbb{Z}\\cup 3\\mathbb{Z}$', size='s')
box(ax, 49, 36, 36, 14, 'resultat', label='sup = un autre\nensemble', size='s')
for cx, role in ((21, 'fixe'), (67, 'resultat')):
    arrow(ax, (cx - 10, 15.5), (cx - 4, 35.5), role); arrow(ax, (cx + 10, 15.5), (cx + 4, 35.5), role)
text(ax, 44, 44, '$\\neq$', 'limite', 'xl', weight='bold')
text(ax, 21, 56, 'contient 2 et 3, pas 5', 'limite', 's')
save(fig, '79-112')
