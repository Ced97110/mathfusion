import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
def mat(x, rows, role):
    for i, vals in enumerate(rows):
        for j, v in enumerate(vals):
            box(ax, x + j * 10, 24 - i * 8, 10, 8, role, label=str(v))
mat(5, [(4, 6), (6, 4)], 'sujet')
mat(63, [(2, 0), (0, 10)], 'autre')
text(ax, 15, 37, r'$A$', 'sujet', 'l'); text(ax, 73, 37, r'$B$', 'autre', 'l')
arrow(ax, (27, 28), (60, 28), 'varie', lw=1.2, both=True)
text(ax, 43.5, 33, r'$B=PAQ$', 'varie', 'm')
text(ax, 43.5, 22.5, r'$P,\,Q$ inversibles', 'varie', 's')
box(ax, 24, 3, 40, 8, 'resultat', label=r'même module $M$')
line(ax, [(15, 15.5), (15, 7), (23.4, 7)], 'resultat'); line(ax, [(73, 15.5), (73, 7), (64.6, 7)], 'resultat')
save(fig, '59-046')
