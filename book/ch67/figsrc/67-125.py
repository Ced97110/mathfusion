import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
ax.set_ylim(22, 100)
text(ax, 44, 96, r'$F=\mathbb{Q}$, $u=\sqrt{2}$, $v=\sqrt{3}$', 'encre', 's')
text(ax, 44, 90, r'une infinité de $a\in F$', 'encre', 's')
# 8 values of a, then three dots for "and so on"
xs = [8 + 7.7 * k for k in range(8)]
target = [0, 2, 1, 3, 2, 4, 0, 1]   # field index reached by each a (disc 1 and disc 4 coincide)
bx = [4 + 17 * k for k in range(5)]
for k, x in enumerate(xs):
    role = 'varie' if k in (1, 4) else 'fixe'
    lab = None
    if k == 1: lab = r'$a$'
    if k == 4: lab = r'$b$'
    disc(ax, x, 82, 2.8, role, label=lab, size='s')
for x in (70, 74, 78):
    ax.add_patch(Circle((x, 82), 0.7, fc=COL['fixe'], ec=COL['fixe'], zorder=2))
for k, x in enumerate(xs):
    t = target[k]
    role = 'varie' if k in (1, 4) else 'fixe'
    arrow(ax, (x, 79.2), (bx[t] + 6, 66.3), role, lw=1.0 if role == 'varie' else 0.5)
for k in range(5):
    if k == 2:
        box(ax, bx[k], 58, 12, 8, 'varie', label=r'$K$', size='s')
    else:
        box(ax, bx[k], 58, 12, 8, 'sujet', label='corps', size='s')
text(ax, 44, 53, r'seulement 5 corps $F(u+av)$', 'sujet', 's')
text(ax, 44, 46, r'$a\neq b$ : même corps $K$', 'varie', 's')
box(ax, 3, 28, 22, 9, 'varie', label=r'$K\ni(a-b)v$', size='s')
box(ax, 28.5, 28, 14, 9, 'varie', label=r'$v\in K$', size='s')
box(ax, 46, 28, 14, 9, 'varie', label=r'$u\in K$', size='s')
box(ax, 63.5, 28, 22, 9, 'resultat', label=r'$F(u,v)=F(u+av)$', size='s')
arrow(ax, (25.2, 32.5), (28.3, 32.5), 'fixe')
arrow(ax, (42.7, 32.5), (45.8, 32.5), 'fixe')
arrow(ax, (60.2, 32.5), (63.3, 32.5), 'fixe')
save(fig, '67-125')
