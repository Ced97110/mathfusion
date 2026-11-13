import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)

def mat(ax, cx, cy, v, role='sujet', size='m', dx=3.6, pad=2.4, h=5.4):
    """Matrice 2x2 v=(a,b,c,d) centrée en (cx,cy). Renvoie la demi-largeur."""
    t1 = text(ax, cx - dx, cy, v[0] + '\n' + v[2], role, size); t1.set_linespacing(1.5)
    t2 = text(ax, cx + dx, cy, v[1] + '\n' + v[3], role, size); t2.set_linespacing(1.5)
    hw = dx + pad
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.2, cy + h), (x, cy + h), (x, cy - h), (x - s * 1.2, cy - h)], role, lw=0.9)
    return hw

items = [('P', ('2', '5', '1', '3'), 'varie', 3.2, 2.4, r'$P$'),
         ('A', ('1', '2', '−1', '1'), 'sujet', 3.6, 2.4, r'$A$'),
         ('Pi', ('3', '−5', '−1', '2'), 'varie', 3.8, 2.6, r'$P^{-1}$'),
         ('B', ('−18', '33', '−11', '20'), 'autre', 5.0, 3.4, r'$B$')]
gap = 2.6
widths = [2 * (it[3] + it[4]) for it in items]
total = sum(widths) + gap * 3 + 7.5 + gap
x = (W - total) / 2
cy = 32
for k, (n, v, role, dx, pad, lab) in enumerate(items):
    hw = dx + pad
    mat(ax, x + hw, cy, v, role, 'm', dx, pad)
    text(ax, x + hw, cy - 11, lab, role, 'm')
    x += 2 * hw + gap
    if k == 2:
        text(ax, x + 2.5, cy, '=', 'encre', 'l')
        x += 7.5 + gap
text(ax, 44, 10, r'donc $A\sim B$', 'resultat', 'l')
save(fig, '43-051')
