import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
cols = [12, 34, 56, 78]
vals = ['4', '3', '1,5', '1']
roles = ['sujet', 'fixe', 'fixe', 'resultat']
acts = ['retirer 1', 'la moitié', 'arrondir']
why = ['car il faut\n$2t<d$', 'car 2 boules\nde même\nrayon $t$', 'car $t$ = des\nerreurs\nentières']
y = 52
text(ax, 2, 65, r'cas $d=4$', 'fixe', 's', ha='left')
for i, c in enumerate(cols):
    box(ax, c - 7, y - 5, 14, 10, roles[i], label=vals[i], size='l')
    if i < 3:
        m = (c + cols[i + 1]) / 2
        arrow(ax, (c + 7.5, y), (cols[i + 1] - 7.5, y), 'varie')
        text(ax, m, y + 8, acts[i], 'varie', 's')
        line(ax, [(m, y - 1.5), (m, 38)], 'fixe', lw=0.5, dash=True)
        text(ax, m, 31, why[i], 'encre', 's')
box(ax, 2, 6, 41, 14, 'limite', label=r'$t=2$ : 2 + 2 = 4, pas < 4', size='s')
box(ax, 45, 6, 41, 14, 'resultat', label=r'$t=1$ : 1 + 1 = 2 < 4', size='s')
save(fig, '68-083')
