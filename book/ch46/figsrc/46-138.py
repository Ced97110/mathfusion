import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def row(ax, x0, y, n, roles, labels=None, st=5.6, w=5.0, h=5.0):
    for k in range(1, n + 1):
        r = roles.get(k)
        box(ax, x0 + (k - 1) * st, y, w, h, r or "fixe", fill=r is not None, dash=r is None,
            label=(labels or {}).get(k), size="s", r=0.6)

fig, ax = canvas(66)
text(ax, 2, 62, "horloge à 7 heures : 7 est premier", 'encre', 'm', ha='left')
for k in range(1, 8):
    y = 52 - (k - 1) * 7.5
    ok = k in (1, 7)
    text(ax, 5, y + 2.5, str(k), 'resultat' if ok else 'limite', 's')
    for j in range(k):
        box(ax, 9 + j * 5.6, y, 5.0, 5.0, 'resultat' if ok else 'limite', fill=ok, dash=not ok, r=0.6)
text(ax, 18, 54.5, '0 seul', 'resultat', 's', ha='left')
text(ax, 50, 7.5 + 2.5, "l'horloge entière", 'resultat', 's', ha='left')
text(ax, 50, 29, 'aucun sous-groupe', 'limite', 's', ha='left')
save(fig, '46-138')
