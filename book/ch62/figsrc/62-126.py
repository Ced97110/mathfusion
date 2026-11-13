import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
u = 8.0; P = u + 1
def bars(y, head, dp, dc):
    text(ax, 3, y + 16, head, 'encre', 's', ha='left')
    text(ax, 3, y + 5, 'degré\nde $f$', 'sujet', 's', ha='left')
    for i in range(dp): box(ax, 24 + i * P, y + 1, u, 8, 'sujet')
    text(ax, 3, y - 7, 'degré du\ncorps sur ℚ', 'resultat', 's', ha='left')
    for i in range(dc): box(ax, 24 + i * P, y - 11, u, 8, 'resultat')
    text(ax, 24 + dp * P + 1, y + 5, str(dp), 'sujet', 'l', ha='left')
    text(ax, 24 + dc * P + 1, y - 7, str(dc), 'resultat', 'l', ha='left')
bars(54, r'$x^4-1$ : corps ℚ($i$), qui contient ℚ', 4, 2)
bars(20, r'$x^3-2$ : corps $E$, qui contient ℚ', 3, 6)
save(fig, '62-126')
