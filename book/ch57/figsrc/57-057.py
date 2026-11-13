import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)

def mat(cx, cy, rows, role):
    text(ax, cx, cy, f'{rows[0][0]}   {rows[0][1]}\n{rows[1][0]}   {rows[1][1]}', role, 'l')
    hx, hy = 8.5, 7.0
    line(ax, [(cx - hx + 1.5, cy - hy), (cx - hx, cy - hy), (cx - hx, cy + hy), (cx - hx + 1.5, cy + hy)], role, lw=1.0)
    line(ax, [(cx + hx - 1.5, cy - hy), (cx + hx, cy - hy), (cx + hx, cy + hy), (cx + hx - 1.5, cy + hy)], role, lw=1.0)

text(ax, 21, 65, 'une règle sur ℤ²', 'sujet', 's', weight='bold')
text(ax, 68, 65, 'une matrice', 'autre', 's', weight='bold')
# quatre entiers : la règle et la matrice se correspondent dans les deux sens
box(ax, 2, 43, 38, 14, 'resultat', label='(3 ; 5) ↦ (6 ; 5)', size='s')
arrow(ax, (41.5, 50), (56, 50), 'resultat', lw=1.4, both=True)
mat(68, 50, ((2, 0), (0, 1)), 'resultat')
text(ax, 44, 37, 'entiers : correspondance', 'resultat', 's')
# un demi : la correspondance casse
box(ax, 2, 19, 38, 14, 'limite', label='(1 ; 0) ↦ (½ ; 0)', size='s')
line(ax, [(41.5, 26), (56, 26)], 'limite', lw=1.2, dash=True)
text(ax, 48.5, 29.5, r'$\times$', 'limite', 'l', weight='bold')
mat(68, 26, (('½', 0), (0, 1)), 'limite')
text(ax, 44, 11, 'un demi : (½ ; 0) sort de ℤ²', 'limite', 's')
save(fig, '57-057')
