import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
oy = 26
for k, (ox, c, title) in enumerate([(23, 4, r'$c=4$'), (65, 0, r'$c=0$')]):
    X = lambda x: ox + 7 * x
    V = lambda v: oy + 2.4 * v
    line(ax, [(ox - 19, oy), (ox + 19, oy)], 'fixe', lw=0.7)
    line(ax, [(X(t / 20), V((t / 20) ** 2)) for t in range(-52, 53)], 'sujet', lw=1.3)
    line(ax, [(ox - 19, V(c)), (ox + 19, V(c))], 'varie', lw=1.8 if c == 0 else 1.2)
    text(ax, ox, oy + 26, title, 'encre', 'm')
    text(ax, ox + 21, V(c) + (1.8 if c == 0 else 0), r'$c$', 'varie', 's')
    text(ax, X(2.6) + 1.5, V(6.76) + 1.5, r'$x^2$', 'sujet', 's', ha='left')
    if c == 4:
        for s in (-2, 2):
            disc(ax, X(s), V(4), 1.4, 'resultat')
        text(ax, X(-2), oy - 4, r'$x=-2$', 'resultat', 's')
        text(ax, X(2), oy - 4, r'$x=2$', 'resultat', 's')
    else:
        disc(ax, ox, oy, 1.5, 'limite')
        text(ax, ox, oy - 4.5, r'$x=0$ interdit', 'limite', 's')
text(ax, 44, 8, '$x^2=c$ et $x\\neq0$ :\nune solution ssi $c\\neq0$', 'resultat', 's')
save(fig, '70-134')
