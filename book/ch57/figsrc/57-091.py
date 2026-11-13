import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, 'dans ℤ : $x$ = 5 et $y$ = 7', 'sujet', 'l')
text(ax, 44, 65.5, '$n$·$x$ = $x$ + … + $x$ ($n$ fois)', 'fixe', 's')
rules = [
    ('règle 1 : $a(x+y)=ax+ay$', '2·(5 + 7) = 24 = 10 + 14'),
    ('règle 2 : $(a+b)x=ax+bx$', '(2 + 3)·5 = 25 = 10 + 15'),
    ('règle 3 : $(ab)x=a(bx)$', '2·(3·5) = 2·15 = 30 = 6·5'),
    ('règle 4 : $1x=x$', '1·5 = 5'),
]
for i, (tag, val) in enumerate(rules):
    y = 48 - i * 14
    text(ax, 2, y + 10.5, tag, 'sujet', 's', ha='left')
    box(ax, 2, y, 84, 8, 'resultat', label=val)
save(fig, '57-091')
