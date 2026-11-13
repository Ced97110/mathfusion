import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 6.0; x0 = 10
text(ax, 44, 46, r'$f(2)=g(2)-g(1)=11-7=4$', 'encre', 'm')
box(ax, x0, 22, 7 * u, 10, 'fixe', label='7')
box(ax, x0 + 7 * u, 22, 4 * u, 10, 'varie', label='4')
brace(ax, x0, x0 + 11 * u, 33, 'sujet', label=r'$g(2)=11$', down=False)
brace(ax, x0, x0 + 7 * u, 22, 'fixe', label=r'$g(1)=7$')
brace(ax, x0 + 7 * u, x0 + 11 * u, 22, 'varie', label=r'$f(2)=4$')
save(fig, '80-274')
