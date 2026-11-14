import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, r'$\forall x,\ x^2\geq0$', 'sujet', 'xl')
labs = [r'$1^2\geq0$', r'$2^2\geq0$', r'$(-3)^2\geq0$', r'$\ldots$']
w, gap, x0 = 19, 2.5, 2.25
for i, lab in enumerate(labs):
    box(ax, x0 + i * (w + gap), 14, w, 10, 'resultat' if i < 3 else 'fixe', label=lab, size='s')
brace(ax, x0, x0 + 3 * (w + gap) + w, 26, 'sujet', label=r'tous les nombres $x$', down=False)
save(fig, '70-068')
