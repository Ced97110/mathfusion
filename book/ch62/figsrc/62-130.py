import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
# F2[x]/(x^3+x+1) : elements c + d r + e r^2 with c, d, e in {0, 1} : 8 elements
text(ax, 44, 74, r'$c+d\,r_1+e\,r_1^2$ avec $c,d,e\in\{0,1\}$', 'sujet', 'm')
els = ['0', '1', r'$r_1$', r'$1+r_1$', r'$r_1^2$', r'$1+r_1^2$', r'$r_1+r_1^2$', r'$1+r_1+r_1^2$']
for i, e in enumerate(els):
    r, c = divmod(i, 4)
    box(ax, 3 + c * 21.5, 50 - r * 18, 19.5, 13, 'sujet', label=e, size='s')
text(ax, 44, 28, '2 × 2 × 2 = 8 éléments', 'encre', 'm')
box(ax, 14, 8, 60, 12, 'varie', label=r'règle : $r_1^3=r_1+1$')
save(fig, '62-130')
