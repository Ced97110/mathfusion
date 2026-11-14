import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, r'$\eta(1)=1^{\prime}$ : neutre sur neutre', 'encre', 'm')
for i, (ttl, tgt, role, lab) in enumerate((('bon renommage', 0, 'resultat', 'r_0'), ('renommage brouillé', 1, 'limite', 'r_1'))):
    y = 28 - 22 * i + 4
    text(ax, 44, y + 12, ttl, role, 's')
    box(ax, 4, y - 5, 24, 10, 'sujet', label='0 (neutre)', size='s')
    arrow(ax, (29, y), (57, y), role, lw=1.4)
    text(ax, 43, y + 3, r'$\eta$', role, 's')
    box(ax, 58, y - 5, 26, 10, 'autre', label=r'$%s$' % lab + (' (neutre)' if tgt == 0 else ''), size='s')
text(ax, 44, 3, 'seul le premier convient', 'resultat', 's') if False else None
save(fig, '45-024')
