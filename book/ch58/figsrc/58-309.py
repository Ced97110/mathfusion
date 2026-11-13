import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
u = 4.6
A = (1, 2, 1); B = (0, 1, -1)
def mk(O, shift):
    def pt(s, t):
        return iso(s * A[0] + t * B[0], s * A[1] + t * B[1], s * A[2] + t * B[2] + shift, O, u)
    return pt
# gauche : plan par O
O1 = (22, 34); p1 = mk(O1, 0)
poly(ax, [p1(-.4, -.4), p1(1.4, -.4), p1(1.4, 1.4), p1(-.4, 1.4)], 'sujet')
disc(ax, O1[0], O1[1], 1.1, 'encre')
text(ax, O1[0] + 6, O1[1] - 1, 'O', 'encre', 's')
text(ax, 22, 63, '−3x + y + z = 0', 'sujet', 's')
box(ax, 2, 4, 40, 10, 'resultat', label='O : 0 = 0, dans le plan', size='s')
# droite : plan décalé de 1
O2 = (66, 34); p2 = mk(O2, 1)
poly(ax, [p2(-.4, -.4), p2(1.4, -.4), p2(1.4, 1.4), p2(-.4, 1.4)], 'limite')
disc(ax, O2[0], O2[1], 1.1, 'encre')
arrow(ax, O2, (O2[0], O2[1] + u), 'varie', lw=1.0)
text(ax, O2[0] + 6, O2[1] - 1, 'O', 'encre', 's')
text(ax, 66, 63, '−3x + y + z = 1', 'limite', 's')
box(ax, 46, 4, 40, 10, 'limite', label='O : 0 ≠ 1, hors du plan', size='s')
text(ax, 44, 22, 'dimension 0, 1, 2 ou 3 ?', 'encre', 's')
save(fig, '58-309')
