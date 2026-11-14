import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def col(cx, head, a, b, role):
    text(ax, cx, 66, head, role, 'm', weight='bold')
    box(ax, cx - 13, 44, 26, 10, role, label=a, dash=(role == 'autre'))
    box(ax, cx - 13, 14, 26, 10, role, label=b, dash=(role == 'autre'))
    arrow(ax, (cx - 6, 43), (cx - 6, 25), 'varie'); arrow(ax, (cx + 6, 25), (cx + 6, 43), 'varie')
    text(ax, cx - 8, 34, 'conj.', 'varie', 's', ha='right'); text(ax, cx + 8, 34, 'conj.', 'varie', 's', ha='left')
col(23, 'complexes', r'$3+4i$', r'$3-4i$', 'sujet')
col(65, 'quaternions', r'$q$', r'$\bar q$', 'autre')
text(ax, 44, 4, 'deux fois : retour au départ', 'resultat', 's')
save(fig, '75-160')
