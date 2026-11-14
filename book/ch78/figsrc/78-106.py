import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(94)
labs = ['ℝ', 'ℂ', 'ℍ', '𝕆', 'dimension 16']
loss = [('rien perdu', 'resultat'), ('perd : commutatif', 'varie'), ('perd : associatif', 'varie'), ('perd : alternatif', 'limite')]
for k, n in enumerate(labs):
    y = 4 + k * 19
    box(ax, 4 + k * 3, y, 26 if k == 4 else 16, 10, 'limite' if k == 4 else 'sujet', label=n, size='l' if k < 4 else 'm')
    if k < 4:
        xa = 12 + k * 3
        arrow(ax, (xa, y + 11), (xa + 3, y + 18), loss[k][1])
        text(ax, xa + 8, y + 14.5, loss[k][0], loss[k][1], 's', ha='left')
save(fig, '78-106')
