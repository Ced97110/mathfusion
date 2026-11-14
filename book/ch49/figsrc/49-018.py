import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cx = [34, 62]
text(ax, 17, 52, '', 'encre', 's')
for x, nm, role in [(cx[0], 'groupe libre', 'sujet'), (cx[1], 'groupe du carré', 'autre')]:
    box(ax, x - 13, 48, 26, 8, role, label=nm, size='s')
rows = [(36, 'une lettre et\nson inverse', [r'$x\,x^{-1}=1$', r'$r\,r^{-1}=1$'], ['sujet', 'autre'], True),
        (18, 'quatre lettres\négales', [r'$xxxx\neq 1$', r'$rrrr=1$'], ['resultat', 'autre'], None)]
for y, lab, cells, roles, _ in rows:
    text(ax, 2, y + 4, lab, 'encre', 's', ha='left')
    for i, (x, c, ro) in enumerate(zip(cx, cells, roles)):
        imposed = (y == 36) or (i == 1)
        box(ax, x - 13, y, 26, 9, ro if imposed else 'resultat', fill=imposed, label=c, size='s', dash=not imposed)
text(ax, 62, 13.5, 'égalité imposée', 'autre', 's')
text(ax, 34, 13.5, 'aucune égalité', 'resultat', 's')
text(ax, 44, 6.5, 'libre : le moins possible', 'encre', 'm', weight='bold')
text(ax, 44, 2.5, 'd’égalités entre mots', 'encre', 'm', weight='bold')
save(fig, '49-018')
