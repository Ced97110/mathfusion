import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import itertools, math
fig, ax = canvas(80)
perms3 = list(itertools.permutations((1, 2, 3)))
assert len(perms3) == math.factorial(3) == 6 and math.factorial(5) == 120
text(ax, 21, 76, r'degré 3 : $3!=6$', 'sujet', 'm', weight='bold')
text(ax, 65, 76, r'degré 5 : $5!=120$', 'autre', 'm', weight='bold')
# left: the six permutations of {1, 2, 3}, written out
for n, p in enumerate(perms3):
    cx, cy = 4 + (n % 2) * 19, 54 - (n // 2) * 13
    box(ax, cx, cy, 17, 9, 'sujet', label=' '.join(map(str, p)), size='m')
# right: 120 squares, 12 by 10
cols, rows, s = 12, 10, 3.2
for n in range(120):
    i, j = n % cols, n // cols
    x0, y0 = 47 + i * s, 20 + j * s
    ax.add_patch(Rectangle((x0, y0), s - 0.5, s - 0.5, ec=COL['autre'], fc=FILL['autre'], lw=0.4, zorder=2))
text(ax, 21, 22, 'les 6 sont permises', 'sujet', 's')
text(ax, 65, 14, 'les 120 sont permises', 'autre', 's')
text(ax, 44, 4, r'groupe de Galois $=S_n$ tout entier', 'encre', 's')
save(fig, '55-140')
