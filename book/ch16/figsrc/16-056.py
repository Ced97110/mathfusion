import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
box(ax, 4, 24, 24, 18, 'sujet', label=r'$x=4$'); box(ax, 58, 50, 26, 10, 'resultat', label=r'$2x=8$'); box(ax, 58, 8, 26, 10, 'limite', label=r'$0=0$')
arrow(ax, (28, 38), (58, 52), 'resultat', both=True); text(ax, 36, 51, r'$\times$ 2 puis $\div$ 2', 'resultat', 's')
text(ax, 71, 64, 'équivalentes', 'resultat', 's')
arrow(ax, (28, 29), (58, 16), 'varie'); text(ax, 52, 27, r'$\times$ 0', 'varie', 'm')
arrow(ax, (58, 11), (28, 25), 'limite'); text(ax, 40, 11, r'$\div$ 0 impossible', 'limite', 's')
text(ax, 71, 3, 'non équivalentes', 'limite', 's')
save(fig, '16-056')
