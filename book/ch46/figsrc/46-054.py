import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 2, 4, 52, 54, 'fixe', label=None)
text(ax, 28, 52, '(ℝ, +)', 'fixe', 'l', weight='bold'); text(ax, 28, 46, 'opération : addition', 'fixe', 's')
box(ax, 9, 10, 38, 28, 'sujet'); text(ax, 28, 30, 'ℝ*', 'sujet', 'l', weight='bold'); text(ax, 28, 22, 'ℝ* est dans ℝ', 'sujet', 's'); text(ax, 28, 15, 'opération : ×', 'sujet', 's')
disc(ax, 70, 46, 6, 'fixe', label='+', size='l'); text(ax, 70, 37, 'celle de G', 'fixe', 's')
disc(ax, 70, 18, 6, 'sujet', label='×', size='l'); text(ax, 70, 9, 'celle de ℝ*', 'sujet', 's')
text(ax, 70, 28, '≠', 'limite', 'xl', weight='bold')
save(fig, '46-054')
