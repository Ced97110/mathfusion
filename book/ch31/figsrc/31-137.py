import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def lbox(ax, x, y, w, h, role, label=None, **k): return box(ax, x, y, w, h, role, label=label, **k)
fig, ax = canvas(46)
text(ax, 44, 41, r'les deux $\times\ 0{,}8660$', 'varie', 's')
for y, nm, a, b in ((20, 'haut', r'$2-1{,}1547$', r'$1{,}7321-1$'), (4, 'bas', r'$2+1{,}1547$', r'$1{,}7321+1$')):
    text(ax, 6, y + 5.5, nm, 'encre', 's')
    lbox(ax, 13, y, 27, 11, 'sujet', a); arrow(ax, (42, y + 5.5), (51, y + 5.5), 'varie'); lbox(ax, 53, y, 28, 11, 'resultat', b)
save(fig, '31-137')
