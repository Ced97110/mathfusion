import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for ox, tag, role, lab in [(4, 'sens direct', 'sujet', r'7 $\times$ 3'), (47, 'sens inverse', 'limite', r'? $\times$ 3')]:
    text(ax, ox + 18, 60, tag, role, 'm', weight='bold')
    box(ax, ox + 5, 36, 28, 12, 'sujet' if ox < 40 else 'fixe', label=lab, size='m')
text(ax, 23, 52, r'$l$ = 7, $w$ = 3', 'sujet', 's')
text(ax, 66, 52, r'$P$ = 20, $w$ = 3', 'sujet', 's')
box(ax, 5, 12, 38, 14, 'resultat', label=r'$P$ = 14 + 6 = 20', size='m')
box(ax, 47, 12, 38, 14, 'limite', label=r'20 = 2$l$ + 6', size='m')
arrow(ax, (24, 34), (24, 26.5), 'resultat')
arrow(ax, (66, 34), (66, 26.5), 'limite')
text(ax, 66, 6, r'$l$ pas lisible', 'limite', 's')
text(ax, 24, 6, r'$P$ se calcule', 'resultat', 's')
save(fig, '16-114')
