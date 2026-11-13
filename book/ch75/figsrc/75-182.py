import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 3, 30, 27, 20, 'sujet')
text(ax, 16.5, 44, r'$Sp_{4}(\mathbb{F}_2)$', 'sujet', 's')
text(ax, 16.5, 36, '720', 'resultat', 'l')
fam = ['groupes alternés', r'$PSL_n(\mathbb{F}_q)$', r'$PSp_{2n}(\mathbb{F}_q)$', 'orthogonaux, unitaires']
text(ax, 62, 74, 'groupes simples finis', 'autre', 'm')
for i, n in enumerate(fam):
    y = 56 - i*14
    box(ax, 40, y, 45, 10, 'autre', label=n, size='s')
    arrow(ax, (30.5, 40), (39.5, y+5), 'varie', lw=0.8)
text(ax, 16.5, 22, 'on compare', 'varie', 's'); text(ax, 16.5, 17, 'les ordres', 'varie', 's')
save(fig, '75-182')
