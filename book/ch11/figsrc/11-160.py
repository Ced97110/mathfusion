import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx = [15, 44, 73]
for x, a, b in zip(cx, ['longueur', 'aire', 'volume'], ['1er degré', '2e degré', '3e degré']):
    text(ax, x, 61, a, 'sujet', 'm'); text(ax, x, 54, b, 'varie', 's')
# degree 1 : one segment
line(ax, [(cx[0] - 9, 36), (cx[0] + 9, 36)], 'sujet', lw=2)
text(ax, cx[0], 41, '$x$', 'sujet', 's')
# degree 2 : rectangle x by x + 3
box(ax, cx[1] - 6, 22, 12, 19.2, 'sujet', r=0.3)
text(ax, cx[1], 45.5, '$x$', 'sujet', 's')
text(ax, cx[1] + 9.5, 31.6, '$x+3$', 'sujet', 's', ha='left')
text(ax, cx[1], 16, r'$x(x+3)=40$', 'resultat', 's')
# degree 3 : box x by x by x
o = (cx[2], 21); u = 11
P = lambda a, b, c: iso(a, b, c, o, u)
poly(ax, [P(0,0,0), P(1,0,0), P(1,0,1), P(0,0,1)], 'sujet')
poly(ax, [P(0,0,0), P(0,1,0), P(0,1,1), P(0,0,1)], 'sujet')
poly(ax, [P(0,0,1), P(1,0,1), P(1,1,1), P(0,1,1)], 'sujet')
text(ax, cx[2] + 7, 21 + 1.5, '$x$', 'sujet', 's')
text(ax, cx[2] - 7, 21 + 1.5, '$x$', 'sujet', 's')
text(ax, cx[2] + 10.5, 21 + 12, '$x$', 'sujet', 's')
save(fig, '11-160')
