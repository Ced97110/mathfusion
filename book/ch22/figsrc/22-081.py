import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def fr(ax, cx, y, num, den, role, w=16, sz="m"):
    text(ax, cx, y + 4, num, role, sz); line(ax, [(cx - w / 2, y), (cx + w / 2, y)], role, lw=0.9); text(ax, cx, y - 4, den, role, sz)

fig, ax = canvas(88)
box(ax, 14, 74, 60, 11, 'sujet', label=r'$\sqrt{36\,a^{7}\,b^{11}}$', size='l')
cols = [(2, r'$36=6^{2}$', r'sort : $6$', 'rien ne reste'),
        (31, r'$a^{7}=a^{6}\times a$', r'sort : $a^{3}$', r'reste : $a$'),
        (60, r'$b^{11}=b^{10}\times b$', r'sort : $b^{5}$', r'reste : $b$')]
for x, d, s, r in cols:
    c = x + 13
    arrow(ax, (c, 73), (c, 66), 'fixe')
    box(ax, x, 55, 26, 10, 'sujet', label=d, size='s')
    arrow(ax, (c, 54), (c, 47), 'resultat')
    box(ax, x, 36, 26, 10, 'resultat', label=s)
    arrow(ax, (c, 35), (c, 28), 'varie')
    box(ax, x, 18, 26, 9, 'varie' if 'reste :' in r else 'fixe', label=r, size='s')
arrow(ax, (44, 17), (44, 11), 'resultat')
box(ax, 14, 1.5, 60, 9, 'resultat', label=r'$6\,a^{3}\,b^{5}\sqrt{ab}$', size='l')
save(fig, '22-081')
