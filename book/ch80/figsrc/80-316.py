import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
for cx, role in ((14, 'sujet'), (44, 'sujet'), (74, 'resultat')):
    disc(ax, cx, 32, 10, role, fill=False, lw=1.1)
    text(ax, cx, 45, r'$A$', role, 'l')
    for dx, l in ((-5, 'a'), (5, 'b')): disc(ax, cx + dx, 32, 3, role, label='$' + l + '$')
text(ax, 29, 32, r'$\times$', 'varie', 'xl'); text(ax, 59, 32, '=', 'encre', 'xl')
text(ax, 44, 14, r'$A \cap A = A$ : rien ne change', 'resultat', 's')
save(fig, '80-316')
