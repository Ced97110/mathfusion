import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
cx = [30, 62]; cy = [22, 58]
names = {(0, 0): '00', (1, 0): '10', (0, 1): '01', (1, 1): '11'}
for (i, j), n in names.items():
    box(ax, cx[i] - 7, cy[j] - 4.5, 14, 9, 'fixe', label=n, size='l')
for j in (0, 1): arrow(ax, (cx[0] + 7, cy[j]), (cx[1] - 7, cy[j]), 'sujet')
for i in (0, 1): arrow(ax, (cx[i], cy[0] + 4.5), (cx[i], cy[1] - 4.5), 'autre')
text(ax, 46, 12, 'chaîne 1 : 0 < 1', 'sujet', 's')
text(ax, 12, 40, 'chaîne 2 : 0 < 1', 'autre', 's', rot=90)
text(ax, 46, 76, r'$\mu=\mu_1\times\mu_2$', 'resultat', 'l')
text(ax, 46, 68, 'sous 11 : les 4 éléments', 'fixe', 's')
save(fig, '80-362')
