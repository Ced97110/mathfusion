import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)

def mat(ax, cx, cy, v, role='sujet', size='m', dx=3.6, pad=2.4, h=5.4):
    """Matrice 2x2 v=(a,b,c,d) centrée en (cx,cy). Renvoie la demi-largeur."""
    t1 = text(ax, cx - dx, cy, v[0] + '\n' + v[2], role, size); t1.set_linespacing(1.5)
    t2 = text(ax, cx + dx, cy, v[1] + '\n' + v[3], role, size); t2.set_linespacing(1.5)
    hw = dx + pad
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.2, cy + h), (x, cy + h), (x, cy - h), (x - s * 1.2, cy - h)], role, lw=0.9)
    return hw

items = [(('1', '0', '0', '1'), 'varie', 3.2, r'$P=I$'), (('1', '2', '−1', '1'), 'sujet', 3.6, r'$A$'),
         (('1', '0', '0', '1'), 'varie', 3.2, r'$P^{-1}=I$'), (('1', '2', '−1', '1'), 'resultat', 3.6, r'$A$')]
gap = 2.6
total = sum(2 * (it[2] + 2.4) for it in items) + gap * 3 + 7.5 + gap
x = (W - total) / 2
cy = 27
for k, (v, role, dx, lab) in enumerate(items):
    hw = dx + 2.4
    mat(ax, x + hw, cy, v, role, 'm', dx)
    text(ax, x + hw, cy - 11, lab, role, 'm')
    x += 2 * hw + gap
    if k == 2:
        text(ax, x + 2.5, cy, '=', 'encre', 'l'); x += 7.5 + gap
text(ax, 44, 42, r'on choisit $P=I$ : rien ne bouge', 'varie', 'm')
save(fig, '43-056')
