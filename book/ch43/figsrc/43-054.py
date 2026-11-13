import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)

def mat(ax, cx, cy, v, role='sujet', size='m', dx=3.6, pad=2.4, h=5.4):
    """Matrice 2x2 v=(a,b,c,d) centrée en (cx,cy). Renvoie la demi-largeur."""
    t1 = text(ax, cx - dx, cy, v[0] + '\n' + v[2], role, size); t1.set_linespacing(1.5)
    t2 = text(ax, cx + dx, cy, v[1] + '\n' + v[3], role, size); t2.set_linespacing(1.5)
    hw = dx + pad
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.2, cy + h), (x, cy + h), (x, cy - h), (x - s * 1.2, cy - h)], role, lw=0.9)
    return hw

mat(ax, 42, 50, ('1', '0', '0', '1'), 'autre', 'm', 3.2)
mat(ax, 72, 50, ('1', '2', '−1', '1'), 'sujet', 'm', 3.6)
text(ax, 42, 61, r'$I$', 'autre'); text(ax, 72, 61, r'$A$', 'sujet')
text(ax, 3, 34, 'a + d', 'encre', ha='left'); text(ax, 3, 22, 'ad − bc', 'encre', ha='left')
text(ax, 42, 34, '2', 'fixe', 'l'); text(ax, 72, 34, '2', 'fixe', 'l')
text(ax, 42, 22, '1', 'limite', 'l'); text(ax, 72, 22, '3', 'limite', 'l')
text(ax, 57, 22, '≠', 'limite', 'l')
text(ax, 44, 8, r'$I$ et $A$ : pas semblables', 'limite', 'm')
save(fig, '43-054')
