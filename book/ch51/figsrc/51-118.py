import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def mat(cx, cy, v, role):
    for sx in (-1, 1):
        x = cx + sx * 8.5
        line(ax, [(x - sx * 1.5, cy + 8), (x, cy + 8), (x, cy - 8), (x - sx * 1.5, cy - 8)], role, lw=1.0)
    ax.text(cx - 3.2, cy, f'{v[0]}\n{v[2]}', color=COL[role], fontsize=SIZE['l'], ha='center', va='center', multialignment='center', zorder=5, linespacing=1.5)
    ax.text(cx + 3.6, cy, f'{v[1]}\n{v[3]}', color=COL[role], fontsize=SIZE['l'], ha='center', va='center', multialignment='center', zorder=5, linespacing=1.5)
text(ax, 5, 44, '$A$', 'sujet', 'l', weight='bold'); mat(20, 44, ['0', '−1', '1', '0'], 'sujet')
text(ax, 5, 14, '$B$', 'autre', 'l', weight='bold'); mat(20, 14, ['2', '0', '0', '1'], 'autre')
text(ax, 45, 44, r'$A\times B=$', 'varie', 'm'); mat(68, 44, ['0', '−1', '2', '0'], 'varie')
text(ax, 45, 14, r'$B\times A=$', 'varie', 'm'); mat(68, 14, ['0', '−2', '1', '0'], 'varie')
text(ax, 68, 29, r'$\neq$', 'limite', 'xl', weight='bold')
save(fig, '51-118')
