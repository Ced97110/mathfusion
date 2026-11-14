import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
def amap(xl, role, tgt, title, note):
    xr = xl + 22
    ys = {1: 32, 2: 14}
    for k in (1, 2):
        disc(ax, xl, ys[k], 3.4, 'sujet', label=str(k), size='s')
        disc(ax, xr, ys[k], 3.4, 'fixe', label=str(k), size='s')
    for k in (1, 2):
        a = (xl + 3.4, ys[k]); b = (xr - 3.4, ys[tgt[k]])
        arrow(ax, a, b, role, lw=0.9)
    text(ax, xl + 11, 48, title, role, 's')
    text(ax, xl + 11, 5, note, role, 's')
amap(8, 'resultat', {1: 2, 2: 1}, 'échange', 'chaque arrivée : 1 départ')
amap(56, 'limite', {1: 1, 2: 1}, 'tout sur 1', "d'où vient 1 ?")
save(fig, '44-115')
