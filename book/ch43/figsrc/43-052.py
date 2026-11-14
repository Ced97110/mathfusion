import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)

def mat(ax, cx, cy, v, role='sujet', size='m', dx=3.6, pad=2.4, h=5.4):
    """Matrice 2x2 v=(a,b,c,d) centrée en (cx,cy). Renvoie la demi-largeur."""
    t1 = text(ax, cx - dx, cy, v[0] + '\n' + v[2], role, size); t1.set_linespacing(1.5)
    t2 = text(ax, cx + dx, cy, v[1] + '\n' + v[3], role, size); t2.set_linespacing(1.5)
    hw = dx + pad
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.2, cy + h), (x, cy + h), (x, cy - h), (x - s * 1.2, cy - h)], role, lw=0.9)
    return hw

mat(ax, 15, 44, ('1', '2', '−1', '1'), 'sujet', 'm', 3.6)
mat(ax, 44, 44, ('−18', '33', '−11', '20'), 'sujet', 'm', 5.0, 3.4)
mat(ax, 73, 44, ('1', '0', '0', '1'), 'autre', 'm', 3.2)
brace(ax, 3, 55, 52.5, 'sujet', label='même classe', down=False)
text(ax, 15, 34, r'$A$', 'sujet'); text(ax, 44, 34, r'$B$', 'sujet'); text(ax, 73, 34, r'$I$', 'autre')
text(ax, 29.5, 22, 'a + d = 2\nad − bc = 3', 'resultat', 'm')
text(ax, 73, 25, 'a + d = 2', 'resultat', 'm')
text(ax, 73, 18, 'ad − bc = 1', 'limite', 'm')
save(fig, '43-052')
