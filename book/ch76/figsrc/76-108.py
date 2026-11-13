import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 4, 57, 'colonnes 1, 2, 3 : vecteur choisi', 'encre', 's', ha='left')
rows = [(['1', '2', '3'], r'$2\times12=24$', 'resultat'),
        (['2', '3', '1'], r'$1\times1=1$', 'resultat'),
        (['1', '2', '1'], r'$e_1\wedge e_1=0$', 'limite')]
for i, (idx, res, rr) in enumerate(rows):
    y = 40 - 15 * i
    for c, k in enumerate(idx):
        role = 'varie' if k == '1' else 'sujet'
        if rr == 'limite' and k == '1': role = 'limite'
        box(ax, 4 + 18 * c, y, 14, 10, role, label=rf'$e_{k}$', size='m')
    arrow(ax, (59, y + 5), (62, y + 5), rr)
    text(ax, 64, y + 5, res, rr, 's', ha='left')
save(fig, '76-108')
