import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(80)
text(ax, 44, 75, 'message : k = 4 bits', 'sujet', 'm')
xs, p = brow(fig, ax, 44, 67, '1001', role='sujet')
brace(ax, xs[0] - p / 2, xs[-1] + p / 2, 63, 'sujet', 'degré 3 au plus')
text(ax, 44, 51, r'$\times$', 'varie', 'xl')
box(ax, 22, 38, 44, 9, 'varie', label=r'$g(x)$ : degré $n-k$ = 3')
arrow(ax, (44, 37), (44, 29), 'varie')
brow(fig, ax, 44, 22, BL * 7, role='resultat')
text(ax, 44, 12, 'mot de n = 7 bits', 'resultat', 'm')
text(ax, 44, 5, 'degré 6 au plus', 'resultat', 's')
save(fig, '68-179')
