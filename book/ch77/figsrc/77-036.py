import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
EM = ' '
def mat(cx, cy, r1, r2, role, hw=9):
    text(ax, cx, cy + 3.2, r1, role, 'm'); text(ax, cx, cy - 3.2, r2, role, 'm')
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.5, cy + 7), (x, cy + 7), (x, cy - 7), (x - s * 1.5, cy - 7)], role)
fig, ax = canvas(104)
mat(22, 92, '2' + EM + '−1', '1' + EM + '2', 'sujet')
mat(66, 92, '2' + EM + '1', '−1' + EM + '2', 'autre')
text(ax, 22, 79, r'$M$ : base $1,\ i$', 'sujet', 's'); text(ax, 66, 79, r'$\Delta^{-1}M\Delta$ : base $i,\ 1$', 'autre', 's')
arrow(ax, (22, 76), (34, 66), 'fixe'); arrow(ax, (66, 76), (54, 66), 'fixe')
box(ax, 4, 53, 80, 12, 'varie', label=r'$\lambda 1-\Delta^{-1}M\Delta=\Delta^{-1}(\lambda 1-M)\Delta$', size='s')
arrow(ax, (22, 52), (22, 43), 'fixe'); arrow(ax, (66, 52), (66, 43), 'fixe')
box(ax, 4, 32, 36, 10, 'resultat', label=r'$\lambda^2-4\lambda+5$', size='s'); box(ax, 48, 32, 36, 10, 'resultat', label=r'$\lambda^2-4\lambda+5$', size='s')
arrow(ax, (22, 31), (34, 22), 'resultat'); arrow(ax, (66, 31), (54, 22), 'resultat')
box(ax, 8, 11, 72, 10, 'resultat', label=r'même $\det(\lambda 1-M)$')
text(ax, 28, 4, r'trace $=4$', 'resultat', 's'); text(ax, 60, 4, r'norme $=5$', 'resultat', 's')
save(fig, '77-036')
