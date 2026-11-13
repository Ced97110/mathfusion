import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
f = numberline(ax, 8, 76, 30, -3, 5, labels=False, arrow_right=True)
line(ax, [(f(0), 30), (f(5) + 5, 30)], 'resultat', lw=2.4)
line(ax, [(f(-3), 30), (f(0), 30)], 'limite', lw=2.4)
for v, r, lab in [(-2, 'limite', '−2'), (0.5, 'resultat', '0,5'), (3, 'resultat', '3')]:
    disc(ax, f(v), 30, 1.5, r); text(ax, f(v), 23, lab, r, 'm')
disc(ax, f(0), 30, 1.7, 'limite', fill=False); text(ax, f(0), 23, '0', 'limite', 'm')
brace(ax, f(-3), f(5), 36, 'sujet', label='ℝ : tous les réels', down=False)
brace(ax, f(0) + 1, f(5), 46, 'resultat', label='> 0 : seulement plus grands que 0', down=False)
text(ax, 44, 8, 'ℝ>0', 'resultat', 'xl')
save(fig, '48-144')
