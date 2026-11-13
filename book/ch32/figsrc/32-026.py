import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
data = [(50, 'fixe', r'$2x+3=7$', '1 solution\n(chapitre 16)'), (30, 'fixe', r'$x^2=4$', 'au plus 2 solutions\n(chapitre 23)'),
        (10, 'sujet', r'$\sin\,\theta=0{,}5$', 'inconnue : un angle\ndans un sinus')]
for y, r, eq, tg in data:
    box(ax, 2, y, 44, 14, r, label=eq, size='l'); box(ax, 50, y, 36, 14, r, label=tg, size='s')
    arrow(ax, (46.5, y + 7), (49.5, y + 7), r)
text(ax, 24, 4.5, 'équation trigonométrique', 'sujet', 's')
save(fig, '32-026')
