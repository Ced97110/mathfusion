import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 22, 50, 'Théorème d’Euler', 'resultat', 'm', weight='bold')
text(ax, 66, 50, 'Sécurité de RSA', 'fixe', 'm', weight='bold')
for k in range(10):
    r, c = divmod(k, 5)
    box(ax, 3 + c * 8, 33 - r * 8, 7, 7, 'resultat')
    if k < 6:
        box(ax, 47 + c * 8, 33 - r * 8, 7, 7, 'fixe')
    else:
        box(ax, 47 + c * 8, 33 - r * 8, 7, 7, 'fixe', fill=False, dash=True, label='?')
text(ax, 22, 19, 'démontré pour tous', 'resultat', 's')
text(ax, 66, 19, 'constat : rien trouvé', 'fixe', 's')
save(fig, '53-081')
