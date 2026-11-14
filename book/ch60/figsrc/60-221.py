import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
u = 9; x0 = 30
text(ax, 14, 66, r'$a=3$', 'sujet', 'l', weight='bold')
def row(parts, y, role, dash=False):
    x = x0
    for p in parts:
        box(ax, x, y, u * p - 1.2, 8, role, label=str(p), dash=dash)
        x += u * p
row([3], 52, 'sujet')
row([2, 1], 40, 'sujet')
row([1, 1, 1], 28, 'sujet')
row([1, 2], 12, 'fixe', dash=True)
text(ax, 14, 16, r'$1+2$', 'fixe', 'm')
text(ax, 73, 16, r'même que $2+1$', 'fixe', 's')
save(fig, '60-221')
