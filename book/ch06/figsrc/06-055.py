import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
cs, x0, y0 = 12, 8, 10
for i in range(4):
    for j in range(3):
        box(ax, x0 + i * cs, y0 + j * cs, cs, cs, 'sujet', r=0.2)
brace(ax, x0, x0 + 4 * cs, y0 + 3 * cs, 'sujet', label=r'$b=4$ colonnes', down=False)
xr = x0 + 4 * cs + 3
line(ax, [(xr, y0), (xr, y0 + 3 * cs)], 'sujet')
text(ax, xr + 2, y0 + 1.5 * cs, r'$d=3$' + '\nlignes', 'sujet', 's', ha='left')
text(ax, 71, 14, r'$b\times d$', 'sujet', 'xl', weight='bold')
text(ax, 71, 5, r'$=4\times3=12$', 'sujet', 'm')
save(fig, '06-055')
