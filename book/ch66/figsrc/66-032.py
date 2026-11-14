import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, R = 24, 31, 13
disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.6)
for a, lab, role in [(0, r'$1$', 'fixe'), (90, r'$i$', 'sujet'), (180, r'$-1$', 'fixe'), (270, r'$-i$', 'sujet')]:
    x = cx + R * math.cos(math.radians(a)); y = cy + R * math.sin(math.radians(a))
    disc(ax, x, y, 2.0, role)
    dx = 5.5 * math.cos(math.radians(a)); dy = 4.5 * math.sin(math.radians(a))
    text(ax, x + dx, y + dy, lab, role, 'm')
bx, bw, bh = 46, 40, 12
box(ax, bx, 46, bw, bh, 'sujet', label=r'1  racines : $i$ et $-i$')
box(ax, bx, 27, bw, bh, 'varie', label=r'2  $(x-i)$ et $(x+i)$')
box(ax, bx, 8, bw, bh, 'resultat', label=r'3  produit : $x^2+1$')
arrow(ax, (bx + bw / 2, 46), (bx + bw / 2, 39.5), 'varie')
arrow(ax, (bx + bw / 2, 27), (bx + bw / 2, 20.5), 'varie')
text(ax, cx, 56, r'$\Phi_4$ : 4 côtés', 'sujet', 's')
save(fig, '66-032')
