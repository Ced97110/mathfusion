import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
x0, cw, ch = 6, 15, 9
cols = [r'$1_S$', 'α', 'β', 'γ']
rws = list(cols)
top = 75
for j in range(5):
    for i in range(5):
        x = x0 + j*cw; y = top - (i+1)*ch
        role, fill = 'fixe', False
        if j == 3 and i >= 1: role, fill = 'sujet', True
        if i == 2 and j >= 1: role, fill = 'varie', True
        if j == 3 and i == 2: role, fill = 'resultat', True
        if i == 0 and j == 3: role, fill = 'sujet', True
        if j == 0 and i == 2: role, fill = 'varie', True
        box(ax, x, y, cw, ch, role, fill=fill, r=0.3, lw=0.6)
text(ax, x0 + cw/2, top - ch/2, '∘', 'encre', 'l')
for k, c in enumerate(cols):
    text(ax, x0 + (k+1)*cw + cw/2, top - ch/2, c, 'sujet' if k == 2 else 'encre', 'm')
    text(ax, x0 + cw/2, top - (k+1)*ch - ch/2, c, 'varie' if k == 1 else 'encre', 'm')
text(ax, x0 + 3*cw + cw/2, top - 2*ch - ch/2, 'γ', 'resultat', 'm', weight='bold')
text(ax, 44, 22, "d'abord : colonne β", 'sujet', 'm')
text(ax, 44, 14, 'puis : ligne α', 'varie', 'm')
text(ax, 44, 6, r'case : α ∘ β = γ', 'resultat', 'm')
save(fig, '44-049')
