import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(92)
# formule : le dénominateur est mis en évidence
text(ax, 30, 84, r'$h=d\,\sin\alpha\,\sin\beta\ \div$', 'encre', 'm')
box(ax, 52, 79.5, 32, 9, 'varie', label=r'$\sin(\beta-\alpha)$', size='m')
text(ax, 68, 74, 'dénominateur', 'varie', 's')
# angle au sommet de 3,25° dessiné exactement
ap = (6, 52)
a = math.radians(3.25)
L = 74
line(ax, [ap, (ap[0] + L, ap[1])], 'sujet', lw=1.2)
line(ax, [ap, (ap[0] + L * math.cos(a), ap[1] + L * math.sin(a))], 'sujet', lw=1.2)
text(ax, 44, 58.5, r'angle au sommet $3{,}25°$', 'sujet', 's')
text(ax, 44, 45.5, r'$\sin 3{,}25°=0{,}05669$ : très petit', 'varie', 's')
# deux divisions
box(ax, 4, 22, 38, 12, 'fixe', label=r'$10\div0{,}05669\approx176{,}4$', size='s')
box(ax, 46, 22, 38, 12, 'fixe', label=r'$10\div0{,}05844\approx171{,}1$', size='s')
text(ax, 44, 38, 'sinus de 3,25° puis de 3,35°', 'fixe', 's')
text(ax, 44, 13, 'écart de 5,3 pour un sinus à peine changé', 'varie', 's')
save(fig, '38-078')
