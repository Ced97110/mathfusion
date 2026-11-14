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
fig, ax = canvas(46)
mta(ax, 6, 22, '$EG$', [['1', '0'], ['0', '0']], 'fixe')
text(ax, 25, 27.5, '−', 'encre', 'l')
mta(ax, 30, 22, '$GE$', [['0', '0'], ['0', '1']], 'fixe')
text(ax, 50, 27.5, '=', 'encre', 'l')
mta(ax, 56, 22, '$H$', HM, 'sujet')
brace(ax, 6, 44, 21, 'fixe', label='calcul déjà fait')
text(ax, 63, 17, 'nom court', 'sujet', 's')
save(fig, '78-002')
