import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
# deux disques : même ensemble de nombres, deux façons de l'engendrer
R = 17
cxA, cxB, cy = 21, 67, 40
for cx, role, ttl in ((cxA, 'sujet', r'$\mathbb{Q}(\sqrt{3},\sqrt{5})$'), (cxB, 'autre', r'$\mathbb{Q}(\sqrt{3}+\sqrt{5})$')):
    ax.add_patch(Circle((cx, cy), R, ec=COL[role], fc=FILL[role], lw=0.9, zorder=1))
    text(ax, cx, cy + R + 4.5, ttl, role, 's')
# A : racines -> somme
pa3, pa5, pag = (cxA - 7, cy - 6), (cxA + 7, cy - 6), (cxA, cy + 8)
for p, lab in ((pa3, r'$\sqrt{3}$'), (pa5, r'$\sqrt{5}$')):
    disc(ax, p[0], p[1], 3.6, 'sujet', label=lab, size='s')
    arrow(ax, (p[0] + (pag[0] - p[0]) * 0.28, p[1] + (pag[1] - p[1]) * 0.28), (pag[0] - (pag[0] - p[0]) * 0.28, pag[1] - (pag[1] - p[1]) * 0.28), 'varie')
disc(ax, pag[0], pag[1], 3.6, 'resultat', label=r'$\gamma$', size='s')
# B : somme -> racines
pb3, pb5, pbg = (cxB - 7, cy - 6), (cxB + 7, cy - 6), (cxB, cy + 8)
disc(ax, pbg[0], pbg[1], 3.6, 'autre', label=r'$\gamma$', size='s')
for p, lab in ((pb3, r'$\sqrt{3}$'), (pb5, r'$\sqrt{5}$')):
    disc(ax, p[0], p[1], 3.6, 'resultat', label=lab, size='s')
    arrow(ax, (pbg[0] + (p[0] - pbg[0]) * 0.28, pbg[1] + (p[1] - pbg[1]) * 0.28), (p[0] - (p[0] - pbg[0]) * 0.28, p[1] - (p[1] - pbg[1]) * 0.28), 'varie')
text(ax, cxA, cy - 15.5 - 6, r'$\gamma = \sqrt{3} + 1\times\sqrt{5}$', 'varie', 's')
text(ax, cxB, cy - 15.5 - 6, r'$\sqrt{5} = (\gamma + 2/\gamma)/2$', 'varie', 's')
text(ax, cxB, cy - 15.5 - 12, r'$\sqrt{3} = (\gamma - 2/\gamma)/2$', 'varie', 's')
text(ax, 44, cy, r'$=$', 'resultat', 'xl')
text(ax, 44, 7, 'chaque corps est contenu dans l\'autre', 'resultat', 's')
save(fig, '63-176')
