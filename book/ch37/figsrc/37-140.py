import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
k = 3.0
O1 = (8, 18); O2 = (52, 18)
poly(ax, [O1, (O1[0] + 6 * k, 18), (O1[0] + 5 * k, 18 + 4 * k)], 'sujet')
line(ax, [O2, (O2[0] + 6 * k, 18)], 'fixe', lw=1.4)
for x in (0, 2, 6): disc(ax, O2[0] + x * k, 18, 1.0, 'sujet')
text(ax, 17, 14, '(6 ; 0)', 'sujet', 's'); text(ax, 24, 33, '(5 ; 4)', 'sujet', 's')
text(ax, 58, 14, '(2 ; 0)', 'sujet', 's'); text(ax, 70, 14, '(6 ; 0)', 'sujet', 's')
text(ax, 18, 7.5, '6 × 4 − 5 × 0 = 24', 'resultat', 's'); text(ax, 18, 2.5, 'aire 12', 'resultat', 's')
text(ax, 64, 7.5, '2 × 0 − 6 × 0 = 0', 'varie', 's'); text(ax, 64, 2.5, 'alignés : aire 0', 'varie', 's')
save(fig, '37-140')
