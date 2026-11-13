import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
T = [12 + 8*i for i in range(9)]
arrow(ax, (4, 46), (84, 46), 'limite', both=True)
for x in T: line(ax, [(x, 44.8), (x, 47.2)], 'limite', lw=0.8)
text(ax, 60, 42, '0', 'limite', 's')
text(ax, 18, 60, 'Dessin écarté', 'limite', 'm', weight='bold')
for a, b in zip([60-8*i for i in range(6)], [52-8*i for i in range(6)]):
    arrow(ax, (a, 47.6), (b, 47.6), 'limite', lw=0.9, curve=0.5)
text(ax, 36, 55, 'toujours un point avant', 'limite', 's')
text(ax, 66, 60, 'interdit : axiome 1', 'limite', 's', weight='bold')
f = numberline(ax, 60, 84, 16, 0, 3, arrow_right=False, role='sujet')
arrow(ax, (84, 16), (86, 16), 'sujet', lw=0.9)
disc(ax, 60, 16, 1.5, 'sujet'); ax.patches[-1].set_zorder(3.5)
text(ax, 18, 30, 'Dessin retenu', 'resultat', 'm', weight='bold')
text(ax, 34, 16, 'rien avant 0', 'resultat', 's')
save(fig, '01-037')
