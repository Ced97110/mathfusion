import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = numberline(ax, 8, 80, 22, -3, 3, arrow_right=False)
for v in (-3, -2, -1, 1, 2, 3):
    disc(ax, f(v), 22, 1.6, 'sujet')
disc(ax, f(0), 22, 1.6, 'limite', fill=False, lw=1.2)
brace(ax, f(-3)-1.5, f(-1)+1.5, 28, 'sujet', down=False, label=r'$F^{*}$')
brace(ax, f(1)-1.5, f(3)+1.5, 28, 'sujet', down=False, label=r'$F^{*}$')
text(ax, f(0), 40, '0 : pas dans', 'limite', 's')
text(ax, f(0), 36.5, r'$F^{*}$', 'limite', 's')
text(ax, f(2)+2, 8, r'$2$ a pour inverse $\frac{1}{2}$', 'resultat', 's')
save(fig, '72-090')
