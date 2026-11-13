import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def row(y, nl, nr, rl, rr, sign):
    for i in range(nl): disc(ax, 6 + i * 4.6, y, 1.8, rl)
    for i in range(nr): disc(ax, 64 + i * 4.6, y, 1.8, rr)
    text(ax, 15, y - 8, str(nl), rl, 'xl'); text(ax, 68, y - 8, str(nr), rr, 'xl')
    text(ax, 44, y - 4, sign, 'resultat', 22, weight='bold')
row(66, 5, 2, 'sujet', 'autre', '>')
row(26, 2, 5, 'autre', 'sujet', '<')
arrow(ax, (44, 50), (44, 40), 'varie', both=True)
text(ax, 48, 45, 'même fait', 'varie', 's', ha='left')
save(fig, '07-055')
