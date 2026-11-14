import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 20, 62, r'$V$ : base', 'fixe', 'm'); text(ax, 66, 62, r'$V^*$ : base duale', 'sujet', 'm')
arrow(ax, (6, 44), (32, 44), 'fixe', lw=1.4); text(ax, 19, 49, r'$e_1$', 'fixe')
arrow(ax, (19, 17), (19, 35), 'fixe', lw=1.4); text(ax, 25, 26, r'$e_2$', 'fixe')
box(ax, 52, 39, 28, 10, 'sujet', label=r'$e_1^*$'); box(ax, 52, 21, 28, 10, 'sujet', label=r'$e_2^*$')
arrow(ax, (36, 44), (50, 44), 'varie', both=True); arrow(ax, (36, 26), (50, 26), 'varie', both=True)
text(ax, 44, 8, r'dim $V^* = 2 = \dim V$', 'resultat', 'l')
save(fig, '71-042')
