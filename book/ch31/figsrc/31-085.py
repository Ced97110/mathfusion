import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
for x0, role, head, formula, verb, res in [
    (3, 'varie', 'équation', r'$2x + 1 = 7$', 'on résout', r'$x = 3$'),
    (47, 'sujet', 'identité', r'$\sin^2 + \cos^2 = 1$', 'on démontre', 'vraie pour tout angle')]:
    w = 38
    box(ax, x0, 6, w, 60, role, dash=False)
    text(ax, x0 + w / 2, 59, head, role, 'l', weight='bold')
    box(ax, x0 + 2, 40, w - 4, 11, 'encre', label=formula, size='m')
    arrow(ax, (x0 + w / 2, 40), (x0 + w / 2, 30), role)
    text(ax, x0 + w / 2, 34.5, verb, role, 's', ha='left') if False else None
    text(ax, x0 + w / 2 + 2, 35, verb, role, 's', ha='left')
    box(ax, x0 + 2, 12, w - 4, 14, 'resultat', label=res, size='m' if len(res) < 8 else 's')
save(fig, '31-085')
