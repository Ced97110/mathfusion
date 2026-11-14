import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
O = {'000': (14, 10), '100': (52, 10), '110': (52, 48), '010': (14, 48)}
I = {'001': (24, 20), '101': (42, 20), '111': (42, 38), '011': (24, 38)}
V = {**O, **I}
E = [('000', '100'), ('100', '110'), ('110', '010'), ('010', '000'), ('001', '101'), ('101', '111'),
     ('111', '011'), ('011', '001'), ('000', '001'), ('100', '101'), ('110', '111'), ('010', '011')]
blue = {'000', '100', '010', '001'}
for a, b in E:
    hot = a == '000' or b == '000'
    line(ax, [V[a], V[b]], 'sujet' if hot else 'fixe', lw=1.5 if hot else 0.8)
off = {'000': (-3, -3.5, 'right'), '100': (3, -3.5, 'left'), '110': (3, 3.5, 'left'), '010': (-3, 3.5, 'right'),
       '001': (2, -3.2, 'left'), '101': (-2, -3.2, 'right'), '111': (-2, 3.2, 'right'), '011': (2, 3.2, 'left')}
for k, (x, y) in V.items():
    disc(ax, x, y, 2.0, 'sujet' if k in blue else 'fixe')
    dx, dy, ha = off[k]
    text(ax, x + dx, y + dy, k, 'sujet' if k in blue else 'fixe', 's', ha=ha)
text(ax, 74, 42, r'$B(000,\,1)$', 'sujet', 'm')
text(ax, 74, 33, '4 sommets bleus', 'sujet', 's')
text(ax, 74, 22, r'$1+n=1+3=4$', 'resultat', 's')
save(fig, '68-063')
