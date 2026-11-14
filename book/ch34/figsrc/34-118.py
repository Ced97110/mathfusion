import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(118)
box(ax, 8, 104, 72, 10, 'sujet', label=r'$\tan 75°=\tan(45°+30°)$', size='m')
fr = [r'$\frac{1+1/\sqrt{3}}{1-1/\sqrt{3}}$', r'$\frac{\sqrt{3}+1}{\sqrt{3}-1}$', r'$\frac{4+2\sqrt{3}}{2}$']
ys = [76, 50, 24]
for yy, t in zip(ys, fr):
    box(ax, 8, yy, 44, 17, 'sujet', label=t, size='l')
arrow(ax, (30, 104), (30, 93), 'varie')
text(ax, 34, 98.5, r'$\tan 45°=1,\ \tan 30°=1/\sqrt{3}$', 'varie', 's', ha='left')
arrow(ax, (30, 76), (30, 67), 'varie')
text(ax, 34, 71.5, r'$\times\sqrt{3}$ en haut et en bas', 'varie', 's', ha='left')
arrow(ax, (30, 50), (30, 41), 'varie')
text(ax, 34, 45.5, r'$\times(\sqrt{3}+1)$ en haut et en bas', 'varie', 's', ha='left')
arrow(ax, (30, 24), (30, 14), 'varie')
text(ax, 34, 19, r'$\div 2$ en haut et en bas', 'varie', 's', ha='left')
text(ax, 54, 84.5, '= 1,5774 / 0,4226', 'fixe', 's', ha='left')
box(ax, 8, 3, 72, 10, 'resultat', label=r'$2+\sqrt{3}$ ≈ 3,732', size='m')
save(fig, '34-118')
