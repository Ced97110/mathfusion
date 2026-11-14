import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, r'$Q=\{e,s_B\}$ agit sur $\mathcal{S}$', 'sujet', 'm')
for x, n, role in [(8, 'A', 'varie'), (34, 'B', 'resultat'), (60, 'C', 'varie')]:
    box(ax, x, 22, 20, 10, role, label=r'$P_%s$' % n)
arrow(ax, (18, 32), (70, 32), 'varie', curve=-0.45, both=True)
text(ax, 44, 48, r'$s_B$ échange $P_A$ et $P_C$', 'varie', 's')
text(ax, 44, 17, r'$e$ et $s_B$ le laissent', 'resultat', 's')
text(ax, 23, 8, r'orbite de taille 1 : $\{P_B\}$', 'resultat', 's')
text(ax, 66, 8, r'orbite de taille 2 : $\{P_A,P_C\}$', 'varie', 's')
save(fig, '50-117')
