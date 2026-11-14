import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
rows = [('départ', r'$n=mk$', 'fixe'),
        ('étape décisive', r'$y^k-1=(y-1)(y^{k-1}+\dots+1)$', 'varie'),
        ('arrivée', r'$x^{p^m}-x$ divise $x^{p^n}-x$', 'resultat')]
ys = [78, 58, 38]
for (t, s, r), y in zip(rows, ys):
    text(ax, 3, y, t, r, 's', ha='left')
    box(ax, 28, y - 6, 58, 12, r, label=s, size='s', lw=1.6 if r == 'varie' else 0.8)
for y in ys[:2]: arrow(ax, (57, y - 7), (57, y - 13), 'fixe')
box(ax, 4, 6, 80, 20, 'sujet', size='s')
text(ax, 44, 20, r'cas : $p=2$, $m=2$, $k=3$, $n=6$', 'sujet', 's')
text(ax, 44, 11, r'$2^6-1=63$ ; $2^2-1=3$ ; $63=3\times21$', 'sujet', 's')
save(fig, '67-112')
