import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 24, 60, 'matrices 2×2', 'limite', 'm')
for (i, j, v) in [(0, 0, '0'), (1, 0, '1'), (0, 1, '0'), (1, 1, '0')]:
    box(ax, 10 + i * 10, 42 - j * 10, 10, 10, 'limite' if v == '1' else 'fixe', label=v, size='l')
text(ax, 24, 26, r'$x^2=0$', 'limite', 'm')
text(ax, 24, 17, r'$x\neq0$ sans inverse', 'limite', 's')
text(ax, 66, 60, 'algèbre à division', 'resultat', 'm')
box(ax, 50, 36, 32, 14, 'resultat', label=r'$x\,x^{-1}=1$', size='l')
text(ax, 66, 28, r'pour tout $x\neq0$', 'resultat', 's')
text(ax, 66, 18, 'ℝ   ℍ   𝕆', 'resultat', 'l')
save(fig, '78-111')
