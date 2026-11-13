import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 3, 48, 20, 10, 'sujet', label=r'$4x^2$')
brace(ax, 3.5, 22.5, 47.4, 'sujet', '1 terme')
text(ax, 56, 53, 'monôme', 'sujet', 'l')
box(ax, 3, 16, 20, 10, 'fixe', label=r'$4x^2$'); box(ax, 26, 16, 14, 10, 'fixe', label='+ 3')
brace(ax, 3.5, 39.5, 15.4, 'limite', '2 termes')
text(ax, 64, 21, 'pas un monôme', 'limite', 'm')
save(fig, '15-058')
