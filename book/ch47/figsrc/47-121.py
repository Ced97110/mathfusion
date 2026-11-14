import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 88, 'g = s : un retournement', 'varie', 'm')
text(ax, 44, 80, 'N : les 4 rotations', 'sujet', 's')
box(ax, 14, 62, 60, 14, 'sujet')
for i, t in enumerate(['1', 'r', 'r²', 'r³']):
    text(ax, 14 + 7.5 + 15 * i, 69, t, 'sujet', 'm')
arrow(ax, (22, 61.5), (22, 41), 'varie'); arrow(ax, (66, 61.5), (66, 41), 'varie')
text(ax, 15, 51, 'sN', 'varie', 'm'); text(ax, 73, 51, 'Ns', 'varie', 'm')
text(ax, 44, 51, '=', 'resultat', 'xl')
box(ax, 14, 26, 60, 14, 'resultat')
for i, t in enumerate(['s', 'rs', 'r²s', 'r³s']):
    text(ax, 14 + 7.5 + 15 * i, 33, t, 'resultat', 'm')
text(ax, 44, 20, 'mêmes 4 retournements', 'resultat', 's')
save(fig, '47-121')
