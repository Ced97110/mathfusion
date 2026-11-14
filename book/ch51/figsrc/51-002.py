import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 8, 52, 72, 12, 'sujet', label=r'$a\times(b+c)=a\times b+a\times c$', size='m')
line(ax, [(14, 52), (14, 11.5)], 'fixe')
rows = [('nombres', '2×(3+4) = 2×3+2×4 = 14'), ('expressions', 'x×(x+2) = x×x + x×2'), ('cadran 4 h', '3×(2+3) = 3×2+3×3 = 3')]
for i, (nom, ex) in enumerate(rows):
    y = 36 - 15 * i
    box(ax, 22, y, 64, 11, 'resultat')
    arrow(ax, (14, y + 5.5), (22, y + 5.5), 'varie')
    text(ax, 25, y + 5.5, nom, 'encre', 's', ha='left', weight='bold')
    text(ax, 62, y + 5.5, ex, 'resultat', 's')
save(fig, '51-002')
