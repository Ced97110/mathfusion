import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def curve(ax, fun, xa, xb, mx, my, role='sujet', dash=False, lw=1.2, n=120):
    xs = [xa + (xb - xa) * i / n for i in range(n + 1)]
    ax.plot([mx(x) for x in xs], [my(fun(x)) for x in xs], color=COL[role], lw=lw, ls='--' if dash else '-', zorder=3)

fig, ax = canvas(70)
box(ax, 2, 59, 84, 9, 'sujet', label='produit −30 et somme 4 ?', size='m')
P = [('1 et −30', '−29'), ('−1 et 30', '29'), ('2 et −15', '−13'), ('−2 et 15', '13'), ('3 et −10', '−7'), ('−3 et 10', '7'), ('5 et −6', '−1'), ('−5 et 6', '1')]
for i, (c, s) in enumerate(P):
    col, row = i % 2, i // 2
    box(ax, 2 + col * 43, 47 - row * 9.5, 41, 7.5, 'fixe', label=c + ' : ' + s, size='s')
box(ax, 2, 4, 84, 9, 'resultat', label='aucune somme ne vaut 4', size='m')
save(fig, '23-090')
