import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def venn(ax, cx, cy, keep):
    r = 14
    disc(ax, cx - 7, cy, r, "sujet", fill=False, lw=1.1); disc(ax, cx + 7, cy, r, "autre", fill=False, lw=1.1)
    text(ax, cx - 17, cy + r + 3, r"$A$", "sujet", "l"); text(ax, cx + 17, cy + r + 3, r"$B$", "autre", "l")
    for x, l in ((cx - 13, "a"), (cx, "b"), (cx + 13, "c")):
        disc(ax, x, cy, 3, "resultat" if l in keep else "fixe", label="$" + l + "$")
fig, ax = canvas(58)
venn(ax, 44, 34, "b")
text(ax, 44, 16, r'dans $A$ et dans $B$ : $b$', 'fixe', 's')
text(ax, 44, 7, r'$AB = A \cap B = \{b\}$', 'resultat', 'l')
save(fig, '80-314')
