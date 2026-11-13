import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
EM = ' '
cw = 9.62  # pitch of 'm' digits joined by 3 em spaces
def row(cx, y, n, role):
    return EM * 3
sep = EM * 3
def cells(x0, y, n_cols, role, ch=8):
    for c in range(n_cols):
        ax.add_patch(Rectangle((x0 + c * cw, y), cw, ch, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    text(ax, x0 + n_cols * cw / 2, y + ch / 2, sep.join(['5'] * n_cols), role, 'm')
fig, ax = canvas(80)
text(ax, 44, 74, r'$N(cu)=c^{n}\,N(u)$', 'encre', 'l')
text(ax, 44, 66, r'$c=3$, $n=2$ (dimension de $\mathbb{C}$), $N(u)=5$', 'encre', 's')
cells(5, 36, 3, 'limite')
text(ax, 20, 28, r'$3\times5=15$ : faux', 'limite', 's')
for j in range(3):
    cells(50, 30 + j * 8, 3, 'resultat')
text(ax, 65, 58, r'$3^2\times5=45$ : vrai', 'resultat', 's')
text(ax, 65, 22, r'$3\times3=3^2$ cases', 'resultat', 's')
text(ax, 44, 8, 'chaque case vaut 5', 'fixe', 's')
save(fig, '77-062')
