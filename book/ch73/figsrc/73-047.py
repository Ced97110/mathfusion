import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 5.5
def panel(ox, horizontal, tx, ok, title):
    oy = 14
    X = lambda x: ox + u*x
    Y = lambda y: oy + u*y
    arrow(ax, (ox-1, oy), (X(6)+3, oy), 'fixe', lw=0.6); arrow(ax, (ox, oy-1), (ox, Y(3)+3), 'fixe', lw=0.6)
    if horizontal: line(ax, [(ox, oy), (X(6), oy)], 'sujet', lw=2.2); text(ax, X(0.6), oy-3.5, r'$U$', 'sujet', 'm')
    else: line(ax, [(ox, oy), (ox, Y(3))], 'sujet', lw=2.2); text(ax, ox-3.5, Y(2.7), r'$U$', 'sujet', 'm')
    role = 'resultat' if ok else 'limite'
    disc(ax, X(3), Y(2), 1.1, 'sujet'); disc(ax, X(tx), Y(2), 1.1, role)
    arrow(ax, (X(3)+1.5, Y(2)), (X(tx)-1.5, Y(2)), role)
    text(ax, X(3), Y(2)+4, '(3, 2)', 'sujet', 's'); text(ax, X(tx)+1, Y(2)+8, f'({tx}, 2)', role, 's')
    text(ax, ox+16, 46, title, role, 's')
panel(5, True, 5, True, 'cisaillement')
panel(50, False, 6, False, 'dilatation ×2')
text(ax, 22, 5, 'déplacement dans $U$', 'resultat', 's'); text(ax, 67, 5, 'déplacement hors de $U$', 'limite', 's')
save(fig, '73-047')
