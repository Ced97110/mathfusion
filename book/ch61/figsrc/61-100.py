import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 4, 62, r'$[E:K]$ : colonnes', 'varie', 's', ha='left')
text(ax, 50, 62, r'$[K:F]$ : lignes', 'sujet', 's', ha='left')
c = 4; yc = 56
for cols, rws in [(2, 3), (5, 2), (1, 1)]:
    top = yc - 5; gx = 24
    text(ax, gx + cols * c / 2, yc - 2, str(cols), 'varie', 'm')
    text(ax, gx - 3, top - rws * c / 2, str(rws), 'sujet', 'm')
    for i in range(cols):
        for j in range(rws):
            box(ax, gx + i * c, top - (j + 1) * c, c, c, 'sujet', r=0.3, lw=0.6)
    text(ax, 60, top - rws * c / 2, rf'${cols}\times{rws}={cols * rws}$', 'resultat', 'l', ha='left')
    yc = top - rws * c - 5
save(fig, '61-100')
