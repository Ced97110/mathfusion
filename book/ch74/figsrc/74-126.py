import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 8, 78, 26, -4, 4, step=1, arrow_right=False, size='m')
for v in range(-4, 5):
    inside = abs(v) <= 2
    disc(ax, f(v), 26, 1.4, 'resultat' if inside else 'limite', fill=inside)
brace(ax, f(-2), f(2), 34, 'sujet', label=r'$2\cos\theta$ entre $-2$ et $2$', down=False)
brace(ax, f(-2), f(2), 15, 'resultat', label='cinq valeurs entières', down=True)
text(ax, f(-3.1), 38, 'impossible', 'limite', 's'); text(ax, f(3.1), 38, 'impossible', 'limite', 's')
save(fig, '74-126')
