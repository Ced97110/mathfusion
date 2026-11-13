import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)

def neq_sign(x, y, role, slash):
    line(ax, [(x - 3, y + 1), (x + 3, y + 1)], role, lw=1.2)
    line(ax, [(x - 3, y - 1), (x + 3, y - 1)], role, lw=1.2)
    if slash: line(ax, [(x - 1.6, y - 2.6), (x + 1.6, y + 2.6)], role, lw=1.2)

# gauche : anneau commutatif (les entiers) -> les deux chemins arrivent au même nombre
text(ax, 21, 67, 'dans ℤ : $ab=ba$', 'resultat', 's', weight='bold')
box(ax, 2, 41, 16, 10, 'sujet', label='3·2')
box(ax, 2, 17, 16, 10, 'sujet', label='2·3')
box(ax, 28, 29, 14, 10, 'resultat', label='6')
arrow(ax, (18.8, 46), (27.4, 36), 'varie', lw=1.1)
arrow(ax, (18.8, 22), (27.4, 32), 'varie', lw=1.1)
text(ax, 21, 9, 'gauche = droite :\nplus de différence', 'resultat', 's')

line(ax, [(44, 6), (44, 62)], 'fixe', lw=0.5, dash=True)

# droite : règles A et B -> deux résultats différents
text(ax, 66, 67, 'règles $A$, $B$ : $ab\\neq ba$', 'varie', 's', weight='bold')
text(ax, 66, 58, 'depuis (1 ; 0)', 'fixe', 's')
box(ax, 47, 41, 20, 10, 'sujet', label='$A$ après $B$', size='s')
box(ax, 47, 17, 20, 10, 'sujet', label='$B$ après $A$', size='s')
box(ax, 72, 41, 14, 10, 'varie', label='(2 ; 1)', size='s')
box(ax, 72, 17, 14, 10, 'varie', label='(1 ; 1)', size='s')
arrow(ax, (67.8, 46), (71.4, 46), 'varie', lw=1.1)
arrow(ax, (67.8, 22), (71.4, 22), 'varie', lw=1.1)
neq_sign(79, 34, 'varie', True)
text(ax, 66, 9, 'les résultats diffèrent', 'varie', 's')
save(fig, '57-114')
