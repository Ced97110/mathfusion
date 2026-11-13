import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [(r'$7$', r'$49\ /\ 49$', '1', 'sujet', 'resultat'), (r'$-3$', r'$9\ /\ 9$', '1', 'sujet', 'resultat'),
        (r'$0{,}5$', r'$0{,}25\ /\ 0{,}25$', '1', 'sujet', 'resultat'), (r'$0$', r'$0\ /\ 0$', '?', 'limite', 'limite')]
for k, (a, m, r, ra, rr) in enumerate(rows):
    y = 48 - 14*k
    box(ax, 6, y, 16, 9, ra, label=a); text(ax, 44, y + 4.5, m)
    box(ax, 62, y, 16, 9, rr, label=r, weight='bold')
    arrow(ax, (23, y + 4.5), (33, y + 4.5), ra); arrow(ax, (55, y + 4.5), (61, y + 4.5), rr)
save(fig, '14-041')
