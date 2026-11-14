import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
ys = [72, 44, 16]
titles = ['ensemble ?', 'opération : parenthèses ?', 'neutre ?']
res = [r'$\mathbb{Z}$ : ensemble donné', r'$(5-3)-2=0$ et $5-(3-2)=4$', 'pas examiné']
roles = ['resultat', 'limite', 'fixe']
verd = ['oui', 'non', '?']
for k, (y, t, l, r, v) in enumerate(zip(ys, titles, res, roles, verd)):
    disc(ax, 7, y, 3.4, r, label=str(k + 1), size='l')
    box(ax, 14, y - 9, 66, 18, r, dash=(r == 'fixe'), fill=(r != 'fixe'))
    text(ax, 47, y + 4, t, r, 's', weight='bold')
    text(ax, 47, y - 3.5, l, r, 's')
    text(ax, 84, y, v, r, 'm', weight='bold')
arrow(ax, (47, 62.5), (47, 54.5), 'resultat', lw=1.4)
line(ax, [(47, 34.5), (47, 26.5)], 'fixe', dash=True)
text(ax, 66, 30.5, "on s'arrête", 'limite', 's')
save(fig, '44-061')
