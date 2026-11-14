import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
disc(ax, 40, 40, 26, 'sujet')
text(ax, 40, 62, r'$P$', 'sujet', 'l')
pa, pb, ps, pm = (29, 49), (51, 49), (29, 29), (51, 29)
for src in (pa, pb):
    for dst in (ps, pm):
        d = math.hypot(dst[0] - src[0], dst[1] - src[1]); ux, uy = (dst[0] - src[0]) / d, (dst[1] - src[1]) / d
        arrow(ax, (src[0] + 4.6 * ux, src[1] + 4.6 * uy), (dst[0] - 4.6 * ux, dst[1] - 4.6 * uy), 'varie', lw=0.8)
disc(ax, *pa, 4, 'sujet', label=r'$a$')
disc(ax, *pb, 4, 'sujet', label=r'$b$')
disc(ax, *ps, 4.4, 'resultat', label=r'$a+b$', size='s')
disc(ax, *pm, 4.4, 'resultat', label=r'$ab$', size='s')
disc(ax, 80, 40, 3.6, 'fixe', label=r'$0$')
text(ax, 80, 33, r'$0\notin P$', 'fixe', 's')
text(ax, 44, 6, r'$a,b\in P \Rightarrow a+b,\ ab\in P$', 'encre', 's')
save(fig, '69-049')
