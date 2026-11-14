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
fig, ax = canvas(50)
text(ax, 44, 46, 'deux matrices → une matrice', 'varie', 'm')
mt(ax, 2, 28, '$E$', EM, 'sujet', nw=7)
mt(ax, 2, 8, '$G$', GM, 'autre', nw=7)
box(ax, 33, 17, 20, 13, 'varie', label='crochet\n$[\\ ,\\ ]$')
arrow(ax, (23, 33.5), (33, 26), 'fixe')
arrow(ax, (23, 13.5), (33, 21), 'fixe')
arrow(ax, (53, 23.5), (59, 23.5), 'varie')
mt(ax, 60, 18, '$H$', HM, 'resultat', nw=7)
save(fig, '78-004')
