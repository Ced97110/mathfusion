import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 8, 66, 72, 10, 'sujet', label=r'$\sqrt{17}\approx4$', size='m')
text(ax, 44, 82, r'car 17 est proche de 16 et $4\times4=16$', 'fixe', 's')
f = numberline(ax, 8, 72, 20, -4, 1, labels=False, arrow_right=False)
for v in range(-4, 2): text(ax, f(v), 14.5, str(v).replace('-', '−'), 'fixe', 's')
for v, lab, form in ((-3.5, '−3,5', r'$(-3-4)/2$'), (0.5, '0,5', r'$(-3+4)/2$')):
    disc(ax, f(v), 20, 1.5, 'resultat')
    text(ax, f(v), 26, lab, 'resultat', 'm', weight='bold'); text(ax, f(v), 33, form, 'sujet', 's')
    arrow(ax, (f(v), 64), (f(v), 36), 'sujet', lw=0.7)
text(ax, 44, 50, r'on remplace $\sqrt{17}$ par 4', 'sujet', 's')
text(ax, 44, 6, r'contrôle des deux solutions de $(-3\pm\sqrt{17})/2$', 'resultat', 's')
save(fig, '10-099')
