import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
for cx, role, a, b, c, d in [(22, 'sujet', r'$5^0$', r'$5^3\ /\ 5^3$', r'$125\ /\ 125$', r'$= 1$'),
                              (66, 'limite', r'$0^0$', r'$0^3\ /\ 0^3$', r'$0\ /\ 0$', 'aucun nombre')]:
    box(ax, cx - 14, 56, 28, 10, role, label=a, size='l')
    text(ax, cx, 45, b); text(ax, cx, 33, c)
    arrow(ax, (cx, 55), (cx, 48.5), role); arrow(ax, (cx, 42), (cx, 36.5), role)
    box(ax, cx - 14, 14, 28, 10, 'resultat' if role == 'sujet' else 'limite', label=d, dash=(role == 'limite'))
    arrow(ax, (cx, 30), (cx, 25), 'resultat' if role == 'sujet' else 'limite')
save(fig, '14-038')
