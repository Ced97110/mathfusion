import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
w, gap = 5.0, 2.6
def bar(y, blocks, role, lab):
    for b in range(blocks):
        x = 8 + b * (4 * w + gap)
        box(ax, x, y, 4 * w, 6, role, fill=True, r=0.6)
        for i in range(1, 4): line(ax, [(x + i * w, y + 0.8), (x + i * w, y + 5.2)], role, lw=0.4)
    text(ax, 4, y + 3, lab, role, 's', ha='left')
text(ax, 44, 61, r'ordre de $a^k$ = $n/d$', 'encre', 'm')
bar(40, 3, 'sujet', '')
bar(22, 2, 'autre', '')
brace(ax, 8, 8 + 4 * w * 3 + gap * 2, 47, 'resultat', label=r'$n/d$ = 3 blocs', down=False)
brace(ax, 8, 8 + 4 * w, 40, 'fixe', label=r'$d$ = 4', down=True)
text(ax, 85, 43, r'$n$ = 12', 'sujet', 's', ha='right')
text(ax, 85, 25, r'$k$ = 8', 'autre', 's', ha='right')
text(ax, 44, 12, r'$d$ = PGCD($k$, $n$)', 'fixe', 's')
text(ax, 44, 5, 'blocs communs de 4 retirés', 'fixe', 's')
save(fig, '46-125')
