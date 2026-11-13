import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
labs = ['A\n0', 'B\n1', 'C\n2', 'D\n3', 'E\n4']
cxs = []
for k, lab in enumerate(labs):
    x = 9 + k * 14
    box(ax, x, 26, 13, 12, 'sujet' if k == 0 else 'resultat' if k == 3 else 'fixe', label=lab)
    cxs.append(x + 6.5)
arrow(ax, (cxs[0], 38.5), (cxs[3], 38.5), 'varie', curve=-0.45, lw=1.3)
text(ax, (cxs[0] + cxs[3]) / 2, 50, '+ 3 crans', 'varie', 's')
text(ax, (cxs[0] + cxs[3]) / 2, 57, '0 + 3 = 3', 'resultat', 'm')
arrow(ax, (cxs[1], 25.5), (cxs[4], 25.5), 'varie', curve=0.45, lw=1.3)
text(ax, (cxs[1] + cxs[4]) / 2, 13, '+ 3 crans', 'varie', 's')
text(ax, (cxs[1] + cxs[4]) / 2, 6, '1 + 3 = 4', 'resultat', 'm')
save(fig, '53-014')
