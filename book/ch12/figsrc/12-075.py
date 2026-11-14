import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# 3/4 : trois parts prises sur quatre parts égales
text(ax, 12, 46.5, '3', 'sujet', 'l'); line(ax, [(8, 43), (16, 43)], 'encre'); text(ax, 12, 39.5, '4', 'varie', 'l')
for c in range(4):
    box(ax, 24 + 10 * c, 38, 10, 10, 'sujet' if c < 3 else 'fixe')
brace(ax, 25, 54, 48, 'sujet', label='a = 3 parts', down=False)
brace(ax, 25, 63, 38, 'varie', label='b = 4 parts égales')
# modèle a/b
text(ax, 12, 21.5, 'a', 'sujet', 'l'); line(ax, [(8, 17.5), (16, 17.5)], 'encre'); text(ax, 12, 13.5, 'b', 'varie', 'l')
text(ax, 28, 22, 'a : un relatif', 'sujet', 's', ha='left')
text(ax, 28, 17, 'b : un relatif', 'varie', 's', ha='left')
text(ax, 28, 12, 'b ≠ 0', 'limite', 's', ha='left')
save(fig, '12-075')
