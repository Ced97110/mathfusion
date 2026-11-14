import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
cx = [17, 49, 74]; w = [26, 18, 18]
text(ax, cx[0], 54, 'neutre (noté 1)', 'fixe', 's', weight='bold')
text(ax, cx[1], 54, 'élément', 'sujet', 's', weight='bold')
text(ax, cx[2], 54, 'résultat', 'sujet', 's', weight='bold')
for y, n, e in [(40, '0', '3'), (26, r'$1_S$', 'α'), (12, 'mot vide', 'ab')]:
    box(ax, cx[0] - w[0]/2, y - 5, w[0], 10, 'fixe', label=n)
    box(ax, cx[1] - w[1]/2, y - 5, w[1], 10, 'sujet', label=e)
    arrow(ax, (cx[1] + 9.5, y), (cx[2] - 9.5, y), 'varie')
    box(ax, cx[2] - w[2]/2, y - 5, w[2], 10, 'sujet', label=e)
save(fig, '44-058')
