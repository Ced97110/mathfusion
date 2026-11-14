import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(76)
s, e = '1100101', '1101000'
r = ''.join(str((int(u) + int(v)) % 2) for u, v in zip(s, e))
assert r == '0001101' and sum(u != v for u, v in zip(s, r)) == 3
text(ax, 2, 69, 'mot envoyé', 'sujet', 's', ha='left')
brow(fig, ax, 58, 69, s, role='sujet')
text(ax, 2, 57, '+ erreur', 'limite', 's', ha='left')
brow(fig, ax, 58, 57, e, roles=['limite' if c == '1' else 'fixe' for c in e])
line(ax, [(2, 49.5), (86, 49.5)], 'fixe')
text(ax, 2, 42, '= mot reçu', 'encre', 's', ha='left')
brow(fig, ax, 58, 42, r, roles=['limite' if u != v else 'sujet' for u, v in zip(s, r)])
text(ax, 58, 32, 'trois bits faux', 'limite', 'm')
arrow(ax, (58, 28.5), (58, 21), 'limite')
box(ax, 33, 8, 50, 12, 'limite', label='reste 0 : rien détecté', size='s')
save(fig, '68-182')
