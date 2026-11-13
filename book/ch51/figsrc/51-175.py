import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
P = {'i': (24, 57), 'j': (38.7, 31.5), 'k': (9.3, 31.5)}
for s, (x, y) in P.items():
    disc(ax, x, y, 4.5, 'sujet', label=rf'${s}$', size='l')
def edge(a, b, r=5.8):
    (x1, y1), (x2, y2) = P[a], P[b]
    d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
    arrow(ax, (x1 + ux * r, y1 + uy * r), (x2 - ux * r, y2 - uy * r), 'varie', lw=1.2)
edge('i', 'j'); edge('j', 'k'); edge('k', 'i')
for y, s in zip([58, 46, 34], ['ij=k', 'jk=i', 'ki=j']):
    text(ax, 66, y, rf'${s}$', 'encre', 'l')
text(ax, 44, 14, r'$2i\times 3j=6k$', 'resultat', 'm')
save(fig, '51-175')
