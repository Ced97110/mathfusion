import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 3.2
text(ax, 44, 61, 'n = x² − y² = (x − y)(x + y)', 'encre', 'm')
text(ax, 44, 55, '55 = 8² − 3² = 5 × 11', 'sujet', 'm')
X0, Y0 = 4, 14
cut = 0
for i in range(8):
    for j in range(8):
        if i >= 5 and j >= 5:
            cut += 1
            continue
        ax.add_patch(Rectangle((X0 + i * u, Y0 + j * u), u, u, ec=COL['sujet'], fc=FILL['sujet'], lw=0.4, zorder=2))
assert cut == 9
ax.add_patch(Rectangle((X0 + 5 * u, Y0 + 5 * u), 3 * u, 3 * u, ec=COL['varie'], fc=FILL['varie'], lw=0.8, ls='--', zorder=2))
text(ax, X0 + 6.5 * u, Y0 + 6.5 * u, 'y²', 'varie', 'm')
brace(ax, X0, X0 + 8 * u, Y0, 'sujet', 'x = 8', size='s')
text(ax, 32.8, Y0 + 4 * u, '=', 'encre', 'l')
RX, RY = 37, Y0 + 1.5 * u
for i in range(11):
    for j in range(5):
        ax.add_patch(Rectangle((RX + i * u, RY + j * u), u, u, ec=COL['resultat'], fc=FILL['resultat'], lw=0.4, zorder=2))
brace(ax, RX, RX + 11 * u, RY, 'resultat', 'x + y = 11', size='s')
text(ax, RX + 11 * u + 3, RY + 2.5 * u, 'x − y = 5', 'resultat', 's', rot=90)
save(fig, '53-187')
