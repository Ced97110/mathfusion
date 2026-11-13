import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
line(ax, [(44, 4), (44, 60)], 'fixe', dash=True)
text(ax, 22, 59, r'$\mathbb{Z}$ : infini', 'sujet', 'm', weight='bold'); text(ax, 66, 59, r'$\mathbb{Z}/7$ : 7 éléments', 'autre', 'm', weight='bold')
numberline(ax, 6, 34, 45, 0, 7, 1, labels=False)
for k in range(7):
    a = math.radians(90 - k * 360 / 7); disc(ax, 66 + 7 * math.cos(a), 45 + 7 * math.sin(a), 1.4, 'autre')
box(ax, 5, 24, 35, 8, 'resultat', label='intègre : oui', size='s'); box(ax, 49, 24, 35, 8, 'resultat', label='intègre : oui', size='s')
box(ax, 5, 12, 35, 8, 'limite', label='corps : non', size='s'); box(ax, 49, 12, 35, 8, 'resultat', label='corps : oui', size='s')
text(ax, 22.5, 6, r'$2\times ?=1$ : aucun entier', 'limite', 's'); text(ax, 66.5, 6, r'$2\times 4=8=1$', 'resultat', 's')
save(fig, '51-125')
