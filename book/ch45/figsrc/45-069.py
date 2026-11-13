import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cs = 9; roles = ['fixe', 'sujet', 'varie', 'autre']; x0, y0 = 4, 14
for i in range(4):
    for j in range(4):
        box(ax, x0 + j * cs, y0 + (3 - i) * cs, cs, cs, roles[(i + j) % 4], r=0.2, lw=0.5)
text(ax, x0 + 2 * cs, 57, 'table sans les noms', 'sujet', 'm')
brace(ax, y0, y0 + 4 * cs, x0 - 1, 'resultat') if False else None
line(ax, [(x0, y0 + 4 * cs), (x0 + 4 * cs, y0)], 'encre', lw=0.9, dash=True)
box(ax, x0, y0 + 2 * cs, 4 * cs, cs, 'encre', fill=False, r=0.2, lw=1.6)
x1 = 46
for k, (y, t, r, tx, ty) in enumerate([(46, '4 lignes : la taille', 'resultat', x0 + 4 * cs, y0 + 3.5 * cs),
                                  (32, 'symétrie : abélien', 'resultat', x0 + 3 * cs, y0 + 1.5 * cs),
                                  (18, 'pas jusqu’au neutre : ordre', 'resultat', x0 + 4 * cs, y0 + 2.5 * cs)]):
    text(ax, x1 + 1, y, t, r, 's', ha='left')
    arrow(ax, (x1, y), (tx + 0.5, ty), r, lw=0.8)
text(ax, 44, 6, r'$\eta$ renomme : la table ne change pas', 'varie', 's')
save(fig, '45-069')
