import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def row(ax, x0, y, n, roles, labels=None, st=5.6, w=5.0, h=5.0):
    for k in range(1, n + 1):
        r = roles.get(k)
        box(ax, x0 + (k - 1) * st, y, w, h, r or "fixe", fill=r is not None, dash=r is None,
            label=(labels or {}).get(k), size="s", r=0.6)

fig, ax = canvas(62)
n = 12
div = [1, 2, 3, 4, 6, 12]; cop = [1, 5, 7, 11]
text(ax, 2, 56, r'$n$ = 12 : 12 nombres', 'fixe', 'm', ha='left')
row(ax, 6, 45, n, {k: 'fixe' for k in range(1, n + 1)}, st=6.0, w=5.4)
text(ax, 2, 36, 'diviseurs de 12 : 6', 'autre', 'm', ha='left')
row(ax, 6, 25, n, {k: 'autre' for k in div}, labels={k: str(k) for k in div}, st=6.0, w=5.4)
text(ax, 2, 16, r'premiers avec 12 : $\varphi$(12) = 4', 'sujet', 'm', ha='left')
row(ax, 6, 5, n, {k: 'sujet' for k in cop}, labels={k: str(k) for k in cop}, st=6.0, w=5.4)
save(fig, '46-130')
