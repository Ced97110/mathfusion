import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax, x, y, n, w, gap, role, label=None, h=None, dash=False):
    xs = []
    for i in range(n):
        xi = x + i * (w + gap); box(ax, xi, y, w, h or w, role, label=label, dash=dash); xs.append(xi + w / 2)
    return xs

fig, ax = canvas(42)
y, w = 16, 10
x0 = 14.5
a1 = x0; a2 = x0 + 13; d0 = x0 + 26; a3 = x0 + 49
for x in (a1, a2, a3): box(ax, x, y, w, w, 'sujet', label='$a$', size='l')
box(ax, d0, y, 20, w, 'varie', label=r'$\cdots$', size='xl', dash=True)
brace(ax, a1, a2 + w, y, 'sujet', 'facteurs écrits')
brace(ax, a3, a3 + w, y, 'sujet', 'dernier facteur')
brace(ax, d0, d0 + 20, y + w, 'varie', 'pas un facteur', down=False)
text(ax, d0 + 10, y + w + 8.5, 'et ainsi de suite', 'varie', 's')
save(fig, '45-113')
