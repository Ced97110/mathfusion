import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 4, 52, 80, 11, 'fixe', label=r'$\sim$  dit seulement : équivalence', size='m')
arrow(ax, (14, 51), (14, 44), 'sujet', lw=1.0)
text(ax, 18, 47.5, 'le signe propre en dit plus', 'sujet', 's', ha='left')
rows = [(30, r'$109 = 1$', 'limite', 'faux : pas le même nombre'),
        (16, r'$109 \equiv 1\ (\mathrm{mod}\ 12)$', 'resultat', 'vrai : même position'),
        (2, r'$\cong$', 'fixe', 'isomorphe : chapitre 45')]
for y, s, r, c in rows:
    box(ax, 4, y, 44, 11, r); text(ax, 26, y + 5.5, s, r, 'm')
    text(ax, 51, y + 5.5, c, r, 's', ha='left')
save(fig, '43-034')
