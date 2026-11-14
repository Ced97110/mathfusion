import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cols = [(2, 'sujet', r'$3+4x$', [('3', '1, 3'), ('4', '1, 2, 4')], '1', 'contenu 1 : primitif', 'resultat'),
        (46, 'autre', r'$2+4x$', [('2', '1, 2'), ('4', '1, 2, 4')], '1, 2', 'contenu 2 : pas primitif', 'autre')]
for x, role, name, coefs, common, verdict, vrole in cols:
    box(ax, x, 56, 40, 11, role, label=name, size='l')
    text(ax, x + 20, 50, 'diviseurs des coefficients', 'fixe', 's')
    for i, (c, divs) in enumerate(coefs):
        y = 38 - i * 11
        box(ax, x, y, 10, 8, role, label=c, size='m')
        text(ax, x + 13, y + 4, divs, 'encre', 'm', ha='left')
    text(ax, x + 20, 22, 'en commun : ' + common, 'varie', 's')
    box(ax, x, 6, 40, 11, vrole, label=verdict, size='s')
save(fig, '54-217')
