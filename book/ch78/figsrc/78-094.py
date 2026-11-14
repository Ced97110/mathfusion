import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 28, 50, r'$Q(x)$', 'sujet', 's'); text(ax, 52, 50, r'$c\,Q(y)$', 'varie', 's'); text(ax, 76, 50, r'$Q(x,y)$', 'resultat', 's')
for k, (cpl, a, b, r) in enumerate([(r'$(1,2)$', '1', r'$(-1)\cdot4$', '5'), (r'$(-4,7)$', '16', r'$(-1)\cdot49$', '65')]):
    y = 28 - k * 17 + 3
    text(ax, 10, y + 5, cpl, 'encre', 's')
    box(ax, 20, y, 16, 10, 'sujet', label=a, size='s'); box(ax, 44, y, 16, 10, 'varie', label=b, size='s'); box(ax, 68, y, 16, 10, 'resultat', label=r, size='s')
    if k == 0:
        text(ax, 40, y + 5, r'$-$', size='l'); text(ax, 64, y + 5, r'$=$', size='l')
text(ax, 44, 5, r'$Q(x,y)=Q(x)-c\,Q(y)$', 'encre', 'm')
save(fig, '78-094')
