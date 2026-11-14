import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 22, 51, 44, 9, 'sujet', label=r'$3\sin x+4\cos x$', size='m')
for cx, ang, s, c, note in [(23, '0°', r'$\sin=0\ ;\ \cos=1$', r'$3\times0+4\times1=4$', 'le nombre devant cos'),
                            (65, '90°', r'$\sin=1\ ;\ \cos=0$', r'$3\times1+4\times0=3$', 'le nombre devant sin')]:
    arrow(ax, (44, 51), (cx, 41), 'varie')
    box(ax, cx - 20, 6, 40, 35, 'fixe')
    text(ax, cx, 36, 'x = ' + ang, 'varie', 'l', weight='bold')
    text(ax, cx, 28, s, 'encre', 's')
    box(ax, cx - 18, 15, 36, 8, 'resultat', label=c, size='s')
    text(ax, cx, 10, note, 'resultat', 's')
save(fig, '35-034')
