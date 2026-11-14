import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
sizes = [1, 4, 4, 2, 4, 1]; d = 3.4; gap = 2.2; pad = 1.1
total = sum(sizes) * d + len(sizes) * 2 * pad + (len(sizes) - 1) * gap
x = (W - total) / 2; y = 30
for n in sizes:
    w = n * d + 2 * pad
    box(ax, x, y - 4, w, 8, 'sujet')
    for i in range(n): disc(ax, x + pad + d / 2 + i * d, y, 1.4, 'sujet')
    text(ax, x + w / 2, y - 8, str(n), 'sujet', 'l', weight='bold')
    x += w + gap
text(ax, W / 2, y + 9, '6 orbites : une boîte chacune', 'fixe', 's')
brace(ax, 4, W - 4, 17, 'resultat', None, depth=2.4)
text(ax, W / 2, 7, r'$1+4+4+2+4+1 = 16$ colorations', 'resultat', 'm', weight='bold')
save(fig, '49-177')
