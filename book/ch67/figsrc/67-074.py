import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
# induction : exponent p (known) -> p^2 -> p^3 -> ... ; each step raises to the power p
text(ax, 44, 51, r'$(a+b)^{p^m} = a^{p^m} + b^{p^m}$', 'sujet', 'm')
labs = [('resultat', 'm = 1\nconnu'), ('sujet', 'm = 2'), ('sujet', 'm = 3')]
for k, (role, t) in enumerate(labs):
    box(ax, 3 + k * 26, 22, 20, 17, role, label=t, size='s')
    if k < 2: arrow(ax, (24 + k * 26, 30.5), (28 + k * 26, 30.5), 'varie', lw=1.4)
text(ax, 83, 30.5, '...', 'sujet', 'l')
brace(ax, 3, 66, 20, 'varie', label=r'de $m$ à $m+1$ : puissance $p$', size='s')
save(fig, '67-074')
