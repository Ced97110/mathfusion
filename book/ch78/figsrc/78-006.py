import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mt(ax, x, y, name, rows, role, nw=9, w=14, h=11):
    """Name then a 2x2 matrix box (all entries in label)."""
    text(ax, x, y + h / 2, name, role, 'm', ha='left')
    box(ax, x + nw, y, w, h, role, label='\n'.join('   '.join(r) for r in rows))

def mta(ax, x, y, name, rows, role, w=14, h=11):
    """2x2 matrix box with its name above."""
    box(ax, x, y, w, h, role, label='\n'.join('   '.join(r) for r in rows))
    text(ax, x + w / 2, y + h + 3, name, role, 'm')

def sq(ax, x, y, s, role):
    poly(ax, [(x, y), (x + s, y), (x + s, y + s), (x, y + s)], role)

ZERO = [['0', '0'], ['0', '0']]
EM = [['0', '1'], ['0', '0']]
GM = [['0', '0'], ['1', '0']]
HM = [['1', '0'], ['0', '−1']]
fig, ax = canvas(56)
def tree(xs, pair, mid, root, title, mlabel, rlabel, mrole, rrole):
    cs = [x + 4.5 for x in xs]
    labs = [('$E$', 'sujet'), ('$E$', 'sujet'), ('$G$', 'autre')]
    for x, (l, r) in zip(xs, labs): box(ax, x, 6, 9, 7, r, label=l)
    mc = (cs[pair[0]] + cs[pair[1]]) / 2
    other = [i for i in range(3) if i not in pair][0]
    rc = (mc + cs[other]) / 2
    line(ax, [(cs[pair[0]], 13), (mc, 22)]); line(ax, [(cs[pair[1]], 13), (mc, 22)])
    box(ax, mc - 6, 22, 12, 8, mrole, label=mlabel)
    line(ax, [(mc, 30), (rc, 38)]); line(ax, [(cs[other], 13), (rc, 38)])
    box(ax, rc - 9, 38, 18, 9, rrole, label=rlabel)
    text(ax, rc, 51, title, 'encre', 'm')
    return rc
r1 = tree([4, 15, 27], (0, 1), None, None, '$[[E,E],G]$', '0', '$=0$', 'fixe', 'resultat')
r2 = tree([49, 60, 72], (1, 2), None, None, '$[E,[E,G]]$', '$H$', '$=-2E$', 'sujet', 'resultat')
text(ax, 42.5, 42.5, '≠', 'limite', 'xl')
save(fig, '78-006')
