import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
xs = [26, 40, 54]
w, h = 12, 10
rowsd = [('sujet', (2, 1, 0), 40, 'somme 3'), ('autre', (1, 5, 5), 14, 'somme 11')]
for role, ks, y, s in rowsd:
    text(ax, 14, y + h / 2, '(' + ', '.join(map(str, ks)) + ')', role, 'm')
    for j, (x, k) in enumerate(zip(xs, ks)):
        if j == 0:
            box(ax, x, y, w, h, role, label=str(k), weight='bold')
        else:
            box(ax, x, y, w, h, 'fixe', fill=False, label=str(k), dash=True)
    text(ax, 71, y + h / 2, s, 'fixe', 's', ha='left')
# premier exposant : on compare
box(ax, xs[0] - 1.5, 11.5, w + 3, 41, 'resultat', fill=False, lw=1.4, r=1.5)
text(ax, xs[0] + w / 2, 32, r'$2>1$', 'resultat', 'l', weight='bold')
brace(ax, xs[1], xs[2] + w, 12, 'fixe', label='pas regardés', down=True)
text(ax, 44, 60, r'$(2,1,0)$ est plus haut', 'sujet', 'l')
save(fig, '55-090')
