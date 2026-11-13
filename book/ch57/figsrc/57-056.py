import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)

def mat(cx, cy, rows, role):
    text(ax, cx, cy, f'{rows[0][0]}   {rows[0][1]}\n{rows[1][0]}   {rows[1][1]}', role, 'l')
    hx, hy = 8.5, 7.0
    line(ax, [(cx - hx + 1.5, cy - hy), (cx - hx, cy - hy), (cx - hx, cy + hy), (cx - hx + 1.5, cy + hy)], role, lw=1.0)
    line(ax, [(cx + hx - 1.5, cy - hy), (cx + hx, cy - hy), (cx + hx, cy + hy), (cx + hx - 1.5, cy + hy)], role, lw=1.0)

A = ((1, 2), (0, 1)); B = ((1, 0), (1, 3))
S = ((2, 2), (1, 4)); P = ((3, 6), (1, 3))
text(ax, 44, 65, 'somme : A + B', 'varie', 's')
mat(11, 52, A, 'sujet'); text(ax, 26, 52, '+', 'encre', 'xl')
mat(41, 52, B, 'autre'); text(ax, 56, 52, '=', 'encre', 'xl')
mat(72, 52, S, 'resultat')
text(ax, 44, 36, 'composée (B puis A) : A × B', 'varie', 's')
mat(11, 22, A, 'sujet'); text(ax, 26, 22, '×', 'encre', 'xl')
mat(41, 22, B, 'autre'); text(ax, 56, 22, '=', 'encre', 'xl')
mat(72, 22, P, 'resultat')
save(fig, '57-056')
