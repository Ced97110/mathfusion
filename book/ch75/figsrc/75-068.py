import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
data = [((3,1,2,1), '3 × 1', '1 × 2', '1'), ((1,0,5,1), '1 × 1', '0 × 5', '1'), ((2,0,0,1), '2 × 1', '0 × 0', '2')]
text(ax, 38, 70, r'$a \times d$', 'sujet', 's'); text(ax, 60, 70, r'$b \times c$', 'varie', 's')
for i, ((a, b, c, d), p1, p2, r) in enumerate(data):
    y = 46 - i * 21
    text(ax, 2, y + 6, f'a={a}, b={b}, c={c}, d={d}', 'encre', 's', ha='left')
    box(ax, 30, y, 17, 12, 'sujet', label=p1)
    line(ax, [(49.5, y + 6), (53.5, y + 6)], 'encre')
    box(ax, 55, y, 17, 12, 'varie', label=p2)
    line(ax, [(74.5, y + 7.5), (77, y + 7.5)], 'encre'); line(ax, [(74.5, y + 4.5), (77, y + 4.5)], 'encre')
    box(ax, 79, y, 8, 12, 'resultat' if r == '1' else 'autre', label=r)
save(fig, '75-068')
