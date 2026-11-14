import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
def sq(x, y, role):
    poly(ax, [(x, y), (x + 3.5, y), (x + 3.5, y + 3.5), (x, y + 3.5)], role)
cs = [15, 44, 73]
text(ax, 44, 53, r'message coupé en blocs de $k=4$ bits', 'autre', 'm')
for c in cs:
    for i in range(4):
        sq(c - 7.75 + i * 4, 44, 'autre')
    arrow(ax, (c, 43), (c, 19), 'varie')
    for i in range(7):
        sq(c - 13.75 + i * 4, 14, 'autre' if i < 4 else 'sujet')
text(ax, 85, 45.8, '…', 'fixe', 'l')
brace(ax, 17.25, 28.75, 19.5, 'sujet', label=r'$n-k=3$', down=False)
text(ax, 44, 6, r'chaque bloc devient un mot de $n=7$ bits', 'sujet', 'm')
save(fig, '68-030')
