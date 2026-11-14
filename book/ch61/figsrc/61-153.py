import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
ox, oy, u = 18, 14, 20
arrow(ax, (ox - 8, oy), (82, oy), 'fixe'); arrow(ax, (ox, oy - 6), (ox, 42), 'fixe')
disc(ax, ox, oy, 1.8, 'sujet'); disc(ax, ox + u, oy, 1.8, 'sujet')
text(ax, ox + 1, oy - 5.5, '(0 ; 0)', 'sujet', 's', ha='right')
text(ax, ox + u + 1, oy - 5.5, '(1 ; 0)', 'sujet', 's')
brace(ax, ox, ox + u, oy + 3.5, 'varie', label='distance 1', down=False)
save(fig, '61-153')
