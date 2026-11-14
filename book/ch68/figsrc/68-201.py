import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(68)
f = numberline(ax, 8, 76, 34, 0, 7, arrow_right=True, size='m')
for k in range(8):
    disc(ax, f(k), 43, 2.6, 'resultat' if k in (0, 7) else 'fixe', fill=k in (0, 7))
text(ax, f(0) + 2, 50, 'départ : 1', 'resultat', 's', ha='center')
text(ax, f(3.5), 50, 'αᵏ ≠ 1 pour k = 1 à 6', 'fixe', 's')
text(ax, f(7) - 1, 50, 'α⁷ = 1', 'resultat', 's')
brace(ax, f(0), f(7), 27, 'sujet', '7 pas, un facteur α par pas')
text(ax, 44, 12, 'retour à 1 : au pas 1 ou au pas 7', 'encre', 's')
text(ax, 44, 5, 'α ≠ 1 : donc au pas 7', 'sujet', 's')
save(fig, '68-201')
