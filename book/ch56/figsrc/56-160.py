import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
assert [c % 2 for c in (1, 2, 2)] == [1, 0, 0]   # x^3 + 2x + 2 mod 2 = x^3
steps = [
    ('départ', 'sujet', r'$f=gh$ avec $f=x^3+2x+2$'),
    ('réduire', 'varie', r'modulo $2$ : $\bar f=x^3$'),
    ('étape décisive', 'autre', r'$\bar g$ et $\bar h$ : puissances de $x$' + '\ntermes constants pairs'),
    ('arrivée', 'limite', r'$4$ divise $a_0=2$ ?' + '\nnon : contradiction'),
]
y = 66
for i, (lab, role, body) in enumerate(steps):
    h = 14
    text(ax, 2, y + h / 2, lab, role, 's', ha='left', weight='bold')
    box(ax, 26, y, 60, h, role, label=body, size='s')
    if i < 3:
        arrow(ax, (56, y - 0.3), (56, y - 6.7), 'fixe')
    y -= h + 7
save(fig, '56-160')
