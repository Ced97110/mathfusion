import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
text(ax, 17, 77, r'racines de $z_1^3$', 'sujet', 's')
text(ax, 71, 77, r'racines de $z_2^3$', 'autre', 's')
ys = (60, 40, 20)
left = (r'$a=-5-w$', r'$aw$', r'$aw^2$')
right = (r'$b=-4+w$', r'$bw$', r'$bw^2$')
for yl in ys:
    for yr in ys:
        line(ax, [(31, yl), (57, yr)], 'fixe', lw=0.5)
good = ((0, 0), (1, 2), (2, 1))
for i, j in good:
    line(ax, [(31, ys[i]), (57, ys[j])], 'resultat', lw=1.8)
for k in range(3):
    box(ax, 3, ys[k] - 5.5, 28, 11, 'sujet', label=left[k], size='s')
    box(ax, 57, ys[k] - 5.5, 28, 11, 'autre', label=right[k], size='s')
text(ax, 44, 6, "9 couples possibles\n3 verts : produit " + r'$21=-3p$', 'resultat', 's')
save(fig, '65-119')
