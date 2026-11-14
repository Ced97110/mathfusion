import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
labs = [r'$G_1$ : 24', r'$G_2$ : 12', r'$G_3$ : 4', r'$G_4$ : 1']
fac = [r'$G_1/G_2$ : 24 ÷ 12 = 2', r'$G_2/G_3$ : 12 ÷ 4 = 3', r'$G_3/G_4$ : 4 ÷ 1 = 4']
for i, lab in enumerate(labs):
    y = 62 - 19 * i
    box(ax, 4, y, 22, 11, 'sujet', label=lab, size='s')
    if i < 3:
        arrow(ax, (15, y - 0.5), (15, y - 7.5), 'resultat')
        text(ax, 30, y - 4, fac[i], 'resultat', 's', ha='left')
line(ax, [(26.5, 67.5), (62, 67.5), (62, 29.5), (26.5, 29.5)], 'limite', dash=True)
text(ax, 65, 52, 'non voisins :', 'limite', 's', ha='left')
text(ax, 65, 47, '24 ÷ 4 = 6', 'limite', 's', ha='left')
text(ax, 65, 42, 'pas un facteur', 'limite', 's', ha='left')
save(fig, '64-028')
