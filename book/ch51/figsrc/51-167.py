import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 3, 60, 'dans les entiers', 'encre', 'm', ha='left')
for i, v in enumerate(range(-2, 3)):
    ro = 'resultat' if abs(v) == 1 else 'limite'
    disc(ax, 10 + 17 * i, 48, 5, ro, label=f'{v}'.replace('-', '−'))
text(ax, 3, 34, 'dans les réels (un corps)', 'encre', 'm', ha='left')
line(ax, [(5, 22), (39, 22)], 'resultat', lw=2.5)
line(ax, [(49, 22), (83, 22)], 'resultat', lw=2.5)
disc(ax, 44, 22, 4, 'limite', label='0')
line(ax, [(66, 20), (66, 24)], 'resultat', lw=1.0)
text(ax, 66, 27, '2', 'resultat', 's')
text(ax, 44, 13, 'dans un corps : non nul = unité', 'resultat', 's') if False else text(ax, 44, 13, 'corps : non nul = unité', 'resultat', 's')
box(ax, 3, 2, 6, 5, 'resultat')
text(ax, 11, 4.5, 'est une unité', 'resultat', 's', ha='left')
box(ax, 46, 2, 6, 5, 'limite')
text(ax, 54, 4.5, 'pas une unité', 'limite', 's', ha='left')
save(fig, '51-167')
