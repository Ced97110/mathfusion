import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(88)
text(ax, 44, 82, 'mot de poids 2 : x + x⁴', 'sujet', 'm')
w = '0100100'
brow(fig, ax, 44, 72, w, roles=['sujet' if c == '1' else 'fixe' for c in w])
arrow(ax, (44, 66), (44, 56), 'varie')
text(ax, 48, 61, r'en $x = \alpha$', 'varie', 's', ha='left')
box(ax, 6, 42, 28, 12, 'sujet', label='α', size='l')
box(ax, 54, 42, 28, 12, 'autre', label='α⁴', size='l')
text(ax, 44, 48, '≠', 'resultat', 'xl')
text(ax, 44, 33, 'somme nulle seulement si égaux', 'encre', 's')
text(ax, 44, 25, 'α = α⁴ : α³ = 1, faux', 'limite', 's')
text(ax, 44, 14, 'donc la somme n’est pas 0', 'resultat', 'm')
save(fig, '68-208')
