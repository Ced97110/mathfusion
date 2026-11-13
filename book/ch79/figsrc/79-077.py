import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
x = numberline(ax, 3, 60.6, 12, 0, 16, step=1, every=4, arrow_right=False)
for v in range(0, 17, 4): disc(ax, x(v), 24, 1.5, 'sujet')
for v in range(0, 13, 6): disc(ax, x(v), 34, 1.5, 'autre')
labs = {10: ('4 + 6', 52), 14: ('8 + 6', 52), 16: ('4 + 12', 58)}
for v in range(0, 17, 2):
    disc(ax, x(v), 46, 1.5, 'resultat')
    if v in labs:
        line(ax, [(x(v), 13.5), (x(v), 44.5)], 'resultat', lw=0.4, dash=True)
        text(ax, x(v), labs[v][1], labs[v][0], 'resultat', 's')
text(ax, 66, 24, 'multiples de 4', 'sujet', 's', ha='left'); text(ax, 66, 34, 'multiples de 6', 'autre', 's', ha='left')
text(ax, 66, 46, 'sommes', 'resultat', 's', ha='left')
text(ax, 44, 72, r'$I_1 + I_2 = \{b_1 + b_2\}$', 'resultat', 'l', weight='bold')
text(ax, 44, 65.5, 'toutes les sommes : les nombres pairs', 'resultat', 's')
save(fig, '79-077')
