import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
FS = ' '
def mat(ax, cx, cy, rows, role='encre', size='m', pitch=4.6, gap=3):
    """Matrix as one text per row; returns (xs, ys) of cell centres and cell pitch."""
    cw = 0.636 * SIZE[size] * 25.4 / 72
    n = len(rows[0]); cell = (2 + gap) * cw; width = n * cell - gap * cw; left = cx - width / 2
    pad = lambda v: str(v).replace('-', '−').rjust(2, FS)
    ys = [cy + (len(rows) - 1) / 2 * pitch - i * pitch for i in range(len(rows))]
    xs = [left + j * cell + 1.3 * cw for j in range(n)]
    for y, r in zip(ys, rows): text(ax, cx, y, (FS * gap).join(pad(v) for v in r), role, size)
    xl, xr, yt, yb = left - 3.2, left + width + 3.2, ys[0] + pitch / 2, ys[-1] - pitch / 2
    line(ax, [(xl + 1, yt), (xl, yt), (xl, yb), (xl + 1, yb)], 'encre'); line(ax, [(xr - 1, yt), (xr, yt), (xr, yb), (xr - 1, yb)], 'encre')
    return xs, ys, cell
def cellbox(ax, x, y, w, h, role):
    box(ax, x - w / 2 + 0.3, y - h / 2 + 0.3, w - 0.6, h - 0.6, role, r=0.3, lw=0.6)
fig, ax = canvas(80)
text(ax, 18, 74, r'$A$', 'sujet', 'l')
xa, ya, cell = mat(ax, 18, 63, [[0, -1], [1, 0]], size='l', pitch=7)
cellbox(ax, xa[0], ya[0], cell, 7, 'sujet'); cellbox(ax, xa[0], ya[1], cell, 7, 'sujet')
cellbox(ax, xa[1], ya[0], cell, 7, 'autre'); cellbox(ax, xa[1], ya[1], cell, 7, 'autre')
text(ax, 18 - 6, 55, r'$a_1$', 'sujet', 's'); text(ax, 18 + 6, 55, r'$a_2$', 'autre', 's')
text(ax, 60, 66, r'$(r,s)$ de $A^tA$ :', 'encre', 's')
text(ax, 60, 60, r'ligne $r$ de $A^t$ = colonne $a_r$', 'sujet', 's')
text(ax, 60, 54.5, r'colonne $s$ de $A$ = $a_s$', 'autre', 's')
text(ax, 44, 45, r'$A^tA$', 'resultat', 'l')
for i in range(2):
    for j in range(2):
        role = 'resultat' if i == j else 'fixe'
        box(ax, 8 + j * 37, 22 - 0 + (1 - i) * 10.5, 36, 10, role,
            label=rf'$\langle a_{i+1},a_{j+1}\rangle={1 if i == j else 0}$', size='s')
text(ax, 44, 13, r'$\langle a_r,a_s\rangle=\delta_{rs}$', 'resultat', 'm', weight='bold')
save(fig, '73-079')
