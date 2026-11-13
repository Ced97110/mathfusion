import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 78, r'$\theta=60^\circ$ : $\cos 2\theta$ vaut toujours $-0{,}5$', 'encre', 's')
forms = [(r'$\cos^2\theta-\sin^2\theta$', 'fixe'), (r'$1-2\sin^2\theta$', 'fixe'), (r'$2\cos^2\theta-1$', 'sujet')]
for i, (f, role) in enumerate(forms):
    y = 56 - i * 15
    box(ax, 2, y, 38, 11, role, label=f, size='s')
    arrow(ax, (40.5, y + 5.5), (46, y + 5.5), 'varie')
    box(ax, 46.5, y, 17, 11, 'resultat', label=r'$-0{,}5$', size='s')
text(ax, 75, 26 + 5.5, 'seulement', 'sujet', 's'); text(ax, 75, 26 + 1.5, 'des cosinus', 'sujet', 's')
arrow(ax, (21, 25.5), (21, 17.5), 'varie')
box(ax, 4, 4, 80, 13, 'resultat', label=r'$\cos 3\theta=4\cos^3\theta-3\cos\theta$', size='s')
save(fig, '34-141')
