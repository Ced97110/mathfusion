import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$\eta$ : échanger les deux nombres', 'varie', 's')
text(ax, 44, 55.5, r'$\zeta$ : $(a\,;\,b)\mapsto(a+b\,;\,b)$', 'varie', 's')
rows = [(32, '3 ; 2', r'$\zeta$', '2 ; 3', r'$\eta$', 'varie', 'varie'),
        (10, '2 ; 1', r'$\eta$', '3 ; 1', r'$\zeta$', 'varie', 'varie')]
for y, mid, l1, end, l2, r1, r2 in rows:
    box(ax, 2, y, 16, 10, 'sujet', label='1 ; 2', size='s')
    box(ax, 36, y, 16, 10, 'fixe', label=mid, size='s')
    box(ax, 70, y, 16, 10, 'autre', label=end, size='s')
    arrow(ax, (18.5, y + 5), (35.5, y + 5), r1)
    arrow(ax, (52.5, y + 5), (69.5, y + 5), r2)
    text(ax, 27, y + 9, l1, r1, 'm')
    text(ax, 61, y + 9, l2, r2, 'm')
text(ax, 78, 27, '≠', 'limite', 'xl', weight='bold')
save(fig, '57-052')
