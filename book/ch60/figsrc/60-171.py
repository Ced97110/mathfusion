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
fig, ax = canvas(66)
box(ax, 6, 52, 34, 9, 'sujet', label=r'$d_1=\lambda-2$', size='s')
box(ax, 46, 52, 34, 9, 'resultat', label=r'$d_2=m=\lambda-2$', size='s')
text(ax, 63, 47, 'le dernier', 'resultat', 's')
text(ax, 44, 38, r'$m\,x=0$ pour tout vecteur $x$', 'resultat', 's')
mat(ax, 14, 22, [['2', '0'], ['0', '2']], 'sujet', cw=8)
text(ax, 27, 22, '−', 'encre', 'l')
mat(ax, 42, 22, [['2', '0'], ['0', '2']], 'varie', cw=8)
text(ax, 56, 22, '=', 'encre', 'l')
mat(ax, 72, 22, [['0', '0'], ['0', '0']], 'resultat', cw=8)
text(ax, 14, 10, r'$T$', 'sujet', 'm')
text(ax, 42, 10, r'$2\cdot1$', 'varie', 'm')
text(ax, 72, 10, r'$m(T)=0$', 'resultat', 's')
save(fig, '60-171')
