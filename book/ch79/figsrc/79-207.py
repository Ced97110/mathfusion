import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def bx(xc, y, w, lab, role):
    box(ax, xc - w / 2, y - 4, w, 8, role, label=lab, size='s')
ys = [28, 42, 56, 70]
ax_ = lambda p, q: ax.plot([p[0], q[0]], [p[1], q[1]], color=COL['fixe'], lw=0.9, zorder=1)
L1 = {1: 12, 2: 44, 3: 76}; L2 = {(1, 2): 20, (1, 3): 44, (2, 3): 68}
for i in (1, 2, 3):
    ax_((44, ys[0]), (L1[i], ys[1]))
    for pr, x in L2.items():
        if i in pr: ax_((L1[i], ys[1]), (x, ys[2]))
for x in L2.values(): ax_((x, ys[2]), (44, ys[3]))
bx(44, ys[0], 10, r'$\varnothing$', 'fixe')
bx(L1[1], ys[1], 12, r'$\{1\}$', 'fixe'); bx(L1[3], ys[1], 12, r'$\{3\}$', 'fixe')
bx(44, ys[1], 26, r'$A\cap B=\{2\}$', 'resultat')
bx(L2[(1, 2)], ys[2], 22, r'$A=\{1,2\}$', 'sujet'); bx(L2[(1, 3)], ys[2], 20, r'$\{1,3\}$', 'fixe'); bx(L2[(2, 3)], ys[2], 22, r'$B=\{2,3\}$', 'autre')
bx(44, ys[3], 36, r'$A\cup B=\{1,2,3\}$', 'resultat')
text(ax, 44, 17, 'droite des réels', 'fixe', 's')
f = numberline(ax, 20, 68, 11, 3, 5, step=1, arrow_right=False)
for v in (3, 5): disc(ax, f(v), 11, 1.6, 'resultat')
text(ax, 10, 11, 'inf', 'resultat', 's'); text(ax, 78, 11, 'sup', 'resultat', 's')
save(fig, '79-207')
