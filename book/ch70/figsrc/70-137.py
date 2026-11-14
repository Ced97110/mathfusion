import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
oy = 36
cases = [(2, 0.375, r'$x=1{,}5$' + '\n' + r'$p(x)>0$', 'deux points', 'resultat'),
         (30, 0.0, r'$x=1$' + '\n' + r'$p(x)=0$', 'un point', 'resultat'),
         (58, -1.875, r'$x=0{,}5$' + '\n' + r'$p(x)<0$', 'aucun point', 'fixe')]
for k, (px, pv, title, res, rr) in enumerate(cases):
    ox = px + 14
    line(ax, [(ox - 12, oy), (ox + 12, oy)], 'fixe', lw=0.7)
    line(ax, [(ox, oy - 18), (ox, oy + 12)], 'fixe', lw=0.7)
    line(ax, [(ox + 11 * t / 20, oy + 8 * (t / 20) ** 2) for t in range(-21, 22)], 'sujet', lw=1.3)
    line(ax, [(ox - 12, oy + 8 * pv), (ox + 12, oy + 8 * pv)], 'varie', lw=1.3 if pv else 2.0)
    if pv > 0:
        for s in (-1, 1):
            disc(ax, ox + s * 11 * pv ** 0.5, oy + 8 * pv, 1.3, 'resultat')
    elif pv == 0:
        disc(ax, ox, oy, 1.3, 'resultat')
    text(ax, ox, oy + 22, title, 'encre', 's')
    text(ax, ox, oy - 24, res, rr, 's')
text(ax, ox - 1.5, oy - 3, r'$y$', 'fixe', 's')
line(ax, [(4, 8), (12, 8)], 'sujet', lw=1.3); text(ax, 14, 8, r'$y^2$', 'sujet', 's', ha='left')
line(ax, [(30, 8), (38, 8)], 'varie', lw=1.3); text(ax, 40, 8, r'$p(x)$', 'varie', 's', ha='left')
save(fig, '70-137')
