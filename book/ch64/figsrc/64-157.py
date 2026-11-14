import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
# gauche : un radical dans la formule
text(ax, 20, 70, 'dans la formule', 'encre', 's')
box(ax, 4, 50, 32, 14, 'sujet', label=r'$\sqrt[3]{2}$')
text(ax, 20, 44, '1 radical', 'sujet', 'm')
# droite : deux étages dans la tour
text(ax, 64, 70, 'dans la tour', 'encre', 's')
bx, bw, bh = 46, 36, 10
box(ax, bx, 52, bw, bh, 'sujet', label=r"$F(z,\sqrt[3]{2})$", size='s')
box(ax, bx, 31, bw, bh, 'varie', label=r'$F(z)$')
box(ax, bx, 10, bw, bh, 'fixe', label=r'$F$ : fractions')
arrow(ax, (bx + bw / 2, 20.3), (bx + bw / 2, 30.7), 'varie')
arrow(ax, (bx + bw / 2, 41.3), (bx + bw / 2, 51.7), 'sujet')
text(ax, bx - 2, 25.5, r'racine de 1', 'varie', 's', ha='right')
text(ax, bx - 2, 46.5, r'racine de 2', 'sujet', 's', ha='right')
text(ax, 64, 3.5, '2 étages', 'varie', 'm')
save(fig, '64-157')
