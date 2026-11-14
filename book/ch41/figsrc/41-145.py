import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# deux premières lignes : force x longueur = travail
for y, (a, b, c) in ((62, ('1 N', '1 m', '1 J')), (42, ('50 N', '20 m', '1 000 J'))):
    box(ax, 6, y, 22, 10, 'sujet', label=a)
    text(ax, 33, y + 5, r'$\times$')
    box(ax, 38, y, 22, 10, 'fixe', label=b)
    text(ax, 65, y + 5, '=')
    box(ax, 70, y, 16, 10, 'resultat', label=c, size='s')
# troisième ligne : force inclinée de 30 degrés
x0, y0 = 6, 14
arrow(ax, (x0, y0), (x0 + 40, y0), 'fixe')
text(ax, x0 + 20, y0 - 4.5, '20 m', 'fixe')
L = 24
a = math.radians(30)
arrow(ax, (x0, y0), (x0 + L * math.cos(a), y0 + L * math.sin(a)), 'sujet', lw=1.2)
text(ax, x0 + 27, y0 + 15.5, '50 N', 'sujet')
pts = [(x0 + 14 * math.cos(a * i / 12), y0 + 14 * math.sin(a * i / 12)) for i in range(13)]
line(ax, pts, 'varie')
text(ax, x0 + 18.5, y0 + 2.6, '30°', 'varie', 's')
arrow(ax, (x0 + 48, y0 + 3), (x0 + 54, y0 + 3), 'fixe', lw=0.7)
box(ax, 58, y0 - 3, 28, 12, 'resultat', label='≈ 866,0 J')
save(fig, '41-145')
