import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
rows = [(46, r'$c=-2$', '−+−+', r'$V=3$'), (24, r'$c=2$', '++++', r'$V=0$')]
xs = [30, 43, 56, 69]
for y, lab, signs, v in rows:
    text(ax, 11, y, lab, 'encre', 's')
    for k, (x, s) in enumerate(zip(xs, signs)):
        box(ax, x - 4, y - 5, 8, 10, 'fixe', label=s, size='m')
        if k < 3 and s != signs[k + 1]:
            arrow(ax, (x + 4.3, y), (xs[k + 1] - 4.3, y), 'varie', lw=1.2, both=True)
    text(ax, 81, y, v, 'varie', 's')
text(ax, 44, 7, r'$V(-2)-V(2)=3-0=3$', 'resultat', 's')
save(fig, '69-059')
