import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax, cx, cy, rows, role='encre', size='m', cw=7.0, P=6.0, lw=0.9):
    r = len(rows); c = len(rows[0]); fs = SIZE[size]
    ls = ((P / (0.3387 * fs)) - 0.2) / 0.8
    for j in range(c):
        t = text(ax, cx + (j - (c - 1) / 2) * cw, cy, '\n'.join(rows[i][j] for i in range(r)), role, size); t.set_linespacing(ls)
    hw = c * cw / 2; hh = r * P / 2 + 0.4
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.2, cy + hh), (x, cy + hh), (x, cy - hh), (x - s * 1.2, cy - hh)], role, lw=lw)
fig, ax = canvas(68)
text(ax, 44, 63, r'$A$ diagonale (2, 3) et $g=\lambda-2$', 'encre', 's')
box(ax, 4, 44, 16, 9, 'sujet', label=r'$u_1$', size='m')
arrow(ax, (20, 48.5), (62, 48.5), 'varie')
text(ax, 41, 52, r'$g\,u_1=(A-2\cdot1)u_1$', 'varie', 's')
box(ax, 66, 44, 18, 9, 'resultat', label=r'$0$', size='m')
box(ax, 4, 28, 16, 9, 'sujet', label=r'$u_2$', size='m')
arrow(ax, (20, 32.5), (62, 32.5), 'varie')
text(ax, 41, 36, r'$g\,u_2=(A-2\cdot1)u_2$', 'varie', 's')
box(ax, 66, 28, 18, 9, 'limite', label=r'$u_2\neq0$', size='m')
text(ax, 22, 15, r'$g(A)=$', 'encre', 'm')
mat(ax, 44, 13, [['0', '0'], ['0', '1']], 'limite', cw=8)
text(ax, 62, 15, r'$\neq 0$', 'limite', 'm')
text(ax, 44, 3, r'$d_s$ ne divise pas $g$', 'limite', 's')
save(fig, '60-172')
