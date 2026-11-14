import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
text(ax, 21, 77, 'E engendré par\nles racines', 'resultat', 's')
text(ax, 65, 77, 'E plus grand\n(avec $\\sqrt{3}$)', 'limite', 's')
# gauche : une flèche par permutation
for x, lab, eta in ((11, 'identité', r'$\eta$'), (31, 'échange', r"$\eta'$")):
    box(ax, x - 9, 56, 18, 9, 'sujet', label=lab, size='s')
    box(ax, x - 6, 36, 12, 9, 'varie', label=eta, size='m')
    arrow(ax, (x, 56), (x, 45.5), 'resultat')
text(ax, 21, 25, '1 permutation\n= 1 automorphisme', 'resultat', 's')
# droite : une permutation, deux automorphismes
box(ax, 54, 56, 22, 9, 'sujet', label='identité', size='s')
box(ax, 48, 36, 14, 9, 'varie', label=r'$\eta_1$', size='m')
box(ax, 68, 36, 14, 9, 'varie', label=r'$\eta_2$', size='m')
arrow(ax, (60, 56), (55, 45.5), 'limite')
arrow(ax, (70, 56), (75, 45.5), 'limite')
text(ax, 55, 30, r'$\sqrt{3}\mapsto\sqrt{3}$', 'limite', 's')
text(ax, 75, 30, r'$\sqrt{3}\mapsto-\sqrt{3}$', 'limite', 's')
text(ax, 65, 20, 'même permutation,\ndeux automorphismes', 'limite', 's')
text(ax, 44, 7, r'$\eta$ : automorphisme de $E$', 'fixe', 's')
line(ax, [(43, 14), (43, 72)], 'fixe', dash=True)
save(fig, '65-006')
