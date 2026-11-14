import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)

def mat(ax, cx, cy, v, role='sujet', size='m', dx=3.6, pad=2.4, h=5.4):
    """Matrice 2x2 v=(a,b,c,d) centrée en (cx,cy). Renvoie la demi-largeur."""
    t1 = text(ax, cx - dx, cy, v[0] + '\n' + v[2], role, size); t1.set_linespacing(1.5)
    t2 = text(ax, cx + dx, cy, v[1] + '\n' + v[3], role, size); t2.set_linespacing(1.5)
    hw = dx + pad
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.2, cy + h), (x, cy + h), (x, cy - h), (x - s * 1.2, cy - h)], role, lw=0.9)
    return hw

mat(ax, 14, 46, ('1', '0', '0', '1'), 'sujet', 'm', 3.2)
mat(ax, 74, 46, ('1', '0', '0', '1'), 'resultat', 'm', 3.2)
arrow(ax, (23, 46), (65, 46), 'varie')
text(ax, 44, 53, r'$P\,I\,P^{-1}$', 'varie', 'm')
text(ax, 44, 39, 'repère $P$, puis retour', 'varie', 's')
text(ax, 44, 24, r'$P\,I\,P^{-1}=P\,P^{-1}=I$', 'encre', 'm')
text(ax, 44, 9, r'la classe de $I$ : $I$ seule', 'resultat', 'm')
save(fig, '43-061')
