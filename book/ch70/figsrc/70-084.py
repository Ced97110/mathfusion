import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
text(ax, 44, 98, 'méthode de Seidenberg (1954)', 'encre', 's')
steps = [(r'courbe $f=0$ : point réel ?', 'sujet'),
         (r'si oui : $P$ plus proche de $O$', 'fixe'),
         (r'$P$ annule $f$ et $q$', 'fixe'),
         (r'$a$ racine de $h=\mathrm{Res}_y(f,q)$', 'fixe'),
         (r'Sturm : racine réelle de $h$ ?', 'fixe'),
         (r'réponse pour la courbe', 'resultat')]
for k, (lab, role) in enumerate(steps):
    y = 80 - 15 * k
    box(ax, 8, y, 72, 10, role, label=lab, size='s')
    if k < 5:
        arrow(ax, (44, y - 0.5), (44, y - 5.5), 'varie')
save(fig, '70-084')
