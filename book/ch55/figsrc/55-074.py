import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, 'variables distinctes', 'sujet', 'm', weight='bold')
rows = [r'$e_1$ : 2 + 3 + 4 = 9', r'$e_2$ : 6 + 8 + 12 = 26', r'$e_3$ : 2 × 3 × 4 = 24']
for i, s in enumerate(rows):
    box(ax, 8, 54 - i * 14, 72, 11, 'sujet', label=s)
line(ax, [(4, 26), (84, 26)], 'fixe', dash=True)
text(ax, 44, 20, 'une variable répétée', 'autre', 'm', weight='bold')
box(ax, 8, 4, 72, 11, 'autre', label=r'carrés : 4 + 9 + 16 = 29')
save(fig, '55-074')
