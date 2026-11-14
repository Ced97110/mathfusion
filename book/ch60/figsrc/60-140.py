import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cw = 7
x0 = 4
text(ax, x0, 74, 'G : 8 éléments', 'sujet', 'm', ha='left', weight='bold')
for k in range(8):
    box(ax, x0 + k * cw, 62, cw - 0.6, 8, 'sujet', r=0.4)
arrow(ax, (x0 + 14, 60.5), (x0 + 14, 48.5), 'varie')
text(ax, x0 + 16, 54.5, r'retirer $\langle g\rangle$ : 4 éléments', 'varie', 's', ha='left')
text(ax, x0, 43.5, 'K : 8 ÷ 4 = 2 éléments', 'autre', 'm', ha='left', weight='bold')
for k in range(2):
    box(ax, x0 + k * cw, 33, cw - 0.6, 8, 'varie', r=0.4)
# loop: if K is not cyclic, start again on K
arrow(ax, (x0 + 2 * cw + 2, 37), (x0 + 8 * cw + 3, 66), 'fixe', curve=0.45)
text(ax, 76, 52, 'sinon, on', 'fixe', 's')
text(ax, 76, 48, 'recommence', 'fixe', 's')
arrow(ax, (x0 + 7, 31.5), (x0 + 7, 21.5), 'resultat')
box(ax, 4, 8, 58, 12, 'resultat', label='K cyclique : on s’arrête', size='s')
save(fig, '60-140')
