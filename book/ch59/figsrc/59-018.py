import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
c = {(0, 0): 4, (0, 1): 6, (1, 0): 6, (1, 1): 4}
cx = lambda col: 14 + col * 14
cy = lambda row: 44 - row * 14
for (r, k), v in c.items():
    role = 'sujet' if r == k else 'varie'
    box(ax, cx(k) - 6, cy(r) - 6, 12, 12, role, label=str(v), size='l')
arrow(ax, (cx(0) + 5, cy(0) - 4), (cx(1) - 5, cy(1) + 4), 'sujet', lw=1.0)
arrow(ax, (cx(1) - 5, cy(0) - 4), (cx(0) + 5, cy(1) + 4), 'varie', lw=1.0)
text(ax, 52, 50, r'$4\times4=16$', 'sujet', 'm', ha='left')
text(ax, 52, 40, r'$6\times6=36$', 'varie', 'm', ha='left')
text(ax, 44, 17, r'$16-36=-20$', 'resultat', 'l')
text(ax, 44, 7, 'aire du parallélogramme : 20', 'fixe', 's')
save(fig, '59-018')
