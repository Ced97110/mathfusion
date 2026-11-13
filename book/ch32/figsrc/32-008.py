import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
angs = ['30°', '150°', '390°', '510°']
labs = ['affiché', 'non affiché', 'non affiché', 'non affiché']
bw, bh, gap = 18, 9, 4
text(ax, 38, 66, 'angles de sinus 0,5', 'encre', 'm')
ytop = 58
cy = []
for i, a in enumerate(angs):
    y = ytop - bh - i * (bh + gap)
    cy.append(y + bh / 2)
    ok = i == 0
    box(ax, 29, y, bw, bh, 'resultat' if ok else 'fixe', fill=ok, label=a, dash=not ok)
    text(ax, 27, y + bh / 2, labs[i], 'resultat' if ok else 'fixe', 's', ha='right')
my = sum(cy) / 4
box(ax, 66, my - 6, 20, 12, 'sujet', label='sinus 0,5')
for i, y in enumerate(cy):
    arrow(ax, (48, y), (65.5, my + (y - my) * 0.35), 'resultat' if i == 0 else 'fixe')
save(fig, '32-008')
