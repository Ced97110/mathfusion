import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, 'boule de rayon 3, mots de 23 bits', 'sujet', 'm', weight='bold')
rows = [(56, 'centre', '', '1'), (47, '1 erreur', '23', '23'),
        (38, '2 erreurs', r'$23\times22\div2$', '253'),
        (29, '3 erreurs', r'$23\times22\times21\div6$', '1771')]
for y, lab, formula, n in rows:
    text(ax, 3, y, lab, 'encre', 's', ha='left')
    if formula: text(ax, 47, y, formula, 'fixe', 's')
    text(ax, 84, y, n, 'sujet', 'm', ha='right', weight='bold')
line(ax, [(60, 23.5), (85, 23.5)], 'fixe', lw=0.8)
text(ax, 3, 17, 'total', 'encre', 's', ha='left')
text(ax, 84, 17, r'2048 $= 2^{11}$', 'resultat', 'l', ha='right', weight='bold')
text(ax, 44, 6, r'$2^{23} \div 2^{11} = 2^{12}$ boules', 'resultat', 'm')
save(fig, '68-224')
