import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx = [22, 36.5, 51, 65.5, 80]
text(ax, 7, 44, r'$n$', 'encre', 'm')
text(ax, 7, 22, r'$\varphi(n)$', 'encre', 's')
for n, c in enumerate(cx):
    even = n % 2 == 0
    box(ax, c - 6.5, 40, 13, 8, 'varie' if even else 'fixe', label=str(n))
    box(ax, c - 6.5, 18, 13, 8, 'resultat', label='0' if even else '1')
    arrow(ax, (c, 40), (c, 26.5), 'fixe')
text(ax, 30, 9, r'noyau $2\mathbb{Z}$ : cases orange', 'varie', 's')
text(ax, 70, 9, r'image $\{0,1\}$', 'resultat', 's')
save(fig, '67-044')
