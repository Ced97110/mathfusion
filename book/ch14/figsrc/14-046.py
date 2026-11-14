import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def cell(x, y, role): ax.add_patch(Rectangle((x, y), 6, 6, ec=COL[role], fc=FILL[role], lw=0.6, zorder=2))
for i in range(3):
    for j in range(3): cell(8 + 6*i, 18 + 6*j, 'sujet')
for i in range(2):
    for j in range(2): cell(50 + 6*i, 18 + 6*j, 'autre')
cell(68, 18, 'autre')
text(ax, 17, 42, '9 carreaux', 'sujet', 's'); text(ax, 62, 42, '5 carreaux', 'autre', 's')
text(ax, 39, 28, r'$\neq$', 'limite', 'xl', weight='bold'); text(ax, 65, 21, '+', 'encre', 'l')
text(ax, 17, 11, r'$(1+2)^2 = 9$', 'sujet'); text(ax, 62, 11, r'$1^2 + 2^2 = 5$', 'autre')
save(fig, '14-046')
