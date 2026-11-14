import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def Dp(v):
    return (v[0] - v[1]) * (v[0] - v[2]) * (v[1] - v[2])

A, B = [1, 2, 3], [2, 1, 3]
assert Dp(A) == -2 and Dp(B) == 2 and Dp(A) ** 2 == Dp(B) ** 2 == 4
fig, ax = canvas(70)
text(ax, 22, 66, 'racines 1, 2, 3', 'sujet', 's')
text(ax, 66, 66, 'racines 2, 1, 3', 'varie', 's')
arrow(ax, (36, 66), (52, 66), 'varie', lw=1.0)
text(ax, 44, 61, 'échange', 'varie', 's')
data = [('D', '−2', '2', 'varie', 'varie'), ('d = D²', '4', '4', 'resultat', 'resultat'), ('a₁, a₂, a₃', '6, 11, 6', '6, 11, 6', 'fixe', 'fixe')]
for k, (name, u, v, ru, rv) in enumerate(data):
    y = 42 - k * 15
    box(ax, 3, y, 36, 10, ru, label='%s = %s' % (name, u), size='s')
    box(ax, 49, y, 36, 10, rv, label='%s = %s' % (name, v), size='s')
    text(ax, 44, y + 5, '≠' if k == 0 else '=', 'varie' if k == 0 else 'resultat', 'l', weight='bold')
text(ax, 44, 7, 'd ne bouge pas : il se lit avec les a', 'resultat', 's')
save(fig, '65-051')
