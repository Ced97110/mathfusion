import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
cw, x0 = 5.2, 3
text(ax, 44, 70, r'$H$ annule les colonnes de $G$', 'encre', 'm', weight='bold')
for y, w, res, role, cap, out in ((52, '1110000', '000', 'resultat', 'colonne de $G$ : mot du code', 'annulé'),
                                  (24, '1000000', '001', 'limite', 'pas une colonne de $G$', 'non nul')):
    for i, c in enumerate(w):
        box(ax, x0 + i * cw, y, cw, 6.5, role, label=c, r=0.5)
    text(ax, x0, y - 5, cap, role, 's', ha='left')
    arrow(ax, (x0 + 7 * cw + 2, y + 3.2), (59, y + 3.2), 'autre', lw=1.1)
    text(ax, 50, y + 8, r'$H$', 'autre', 'l', weight='bold')
    box(ax, 61, y - 1, 24, 8.5, role, label=rf'$Hx = {res}$')
    text(ax, 73, y - 5, out, role, 's')
save(fig, '68-136')
