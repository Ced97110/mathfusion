import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(40)
def radical(ox, oy, lab):
    line(ax, [(ox, oy + 4), (ox + 2.5, oy + 3), (ox + 6, oy), (ox + 10.5, oy + 11)], 'fixe', lw=1.6)
    line(ax, [(ox + 10.5, oy + 11), (ox + 33, oy + 11)], 'fixe', lw=1.6)
    box(ax, ox + 12, oy, 20, 8, 'sujet', label=lab)
    text(ax, ox + 22, oy - 4, 'radicande', 'sujet', 's')
radical(6, 10, '16')
radical(46, 10, r'$x + 5$')
text(ax, 44, 32, 'ce qui est sous le trait', 'sujet', 's')
save(fig, '22-032')
