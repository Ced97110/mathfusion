import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
text(ax, 44, 44, r'$3-5$', 'sujet', 'xl')
for i in range(5):
    x = 14 + i * 12
    if i < 3:
        box(ax, x, 18, 10, 10, 'sujet'); disc(ax, x + 5, 23, 3, 'sujet')
    else:
        box(ax, x, 18, 10, 10, 'limite', fill=False, dash=True)
brace(ax, 14, 48, 28, 'sujet', label='3 billes dans le sac', down=False)
brace(ax, 50, 72, 18, 'limite', label='il manque 2')
text(ax, 44, 8, '5 billes demandées', 'varie', 'm')
save(fig, '13-001')
