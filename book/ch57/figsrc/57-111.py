import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, '$A$ : ($p$ ; $q$) ↦ ($p+q$ ; $q$), $a=A$\n$B$ : ($p$ ; $q$) ↦ ($p$ ; $p+q$), $b=B$', 'encre', 's')
def chain(yc, cap, role_cap, vals, ops, role_end):
    text(ax, 2, yc + 11, cap, role_cap, 's', ha='left', weight='bold')
    for i, v in enumerate(vals):
        role = role_end if i == 2 else 'fixe'
        box(ax, 3 + 33 * i, yc - 5, 16, 10, role, label=v, size='s')
    for i, o in enumerate(ops):
        x0 = 19.5 + 33 * i
        arrow(ax, (x0, yc), (x0 + 16, yc), 'varie')
        text(ax, x0 + 8, yc + 4.5, o, 'varie', 's')
chain(40, r'à gauche : $(ab)x=a(bx)$', 'sujet', ['(1 ; 0)', '(1 ; 1)', '(2 ; 1)'], ['1er : $B$', '2e : $A$'], 'sujet')
chain(14, r'à droite : $x(ab)=(xa)b$', 'autre', ['(1 ; 0)', '(1 ; 0)', '(1 ; 1)'], ['1er : $A$', '2e : $B$'], 'autre')
x, y = 77, 27.5
line(ax, [(x - 3, y + 1), (x + 3, y + 1)], 'limite', lw=1.2)
line(ax, [(x - 3, y - 1), (x + 3, y - 1)], 'limite', lw=1.2)
line(ax, [(x - 1.6, y - 2.6), (x + 1.6, y + 2.6)], 'limite', lw=1.2)
save(fig, '57-111')
