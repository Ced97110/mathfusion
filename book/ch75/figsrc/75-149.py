import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'$x=y=(1,\,0)$ et $a=i$', 'encre', 'm')
def row(y, e, r, ro, tag):
    box(ax, 2, y, 32, 10, ro, label=e)
    arrow(ax, (35, y + 5), (45, y + 5), ro)
    box(ax, 46, y, 40, 10, ro, label=r, weight='bold')
    if tag: text(ax, 44, y - 3.6, tag, ro, 's')
row(46, r'$H(x,\,y)$', r'$=1$', 'fixe', None)
row(26, r'$H(ix,\,y)$', r'$=i\times 1=i$', 'sujet', r'$i$ sort à gauche, inchangé')
row(6, r'$H(x,\,iy)$', r'$=\bar{i}\times 1=-i$', 'varie', r'$i$ sort à droite, conjugué')
save(fig, '75-149')
