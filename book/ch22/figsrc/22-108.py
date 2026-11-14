import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
for cx, a, b in ((24, '$4=4$', '$16=16$'), (64, '$a=b$', '$a^2=b^2$')):
    box(ax, cx - 17, 44, 34, 10, 'sujet', label=a)
    arrow(ax, (cx, 44), (cx, 32), 'varie'); text(ax, cx + 3, 38, 'au carré', 'varie', 's', ha='left')
    box(ax, cx - 17, 22, 34, 10, 'resultat', label=b)
text(ax, 44, 10, r'$a=\sqrt{y-3}$ et $b=4$', 'fixe', 's')
save(fig, '22-108')
