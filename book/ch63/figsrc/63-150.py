import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, '(στ)(j²r) = σ(τ(j²r))', 'sujet', 'l', weight='bold')
xs = [2, 33, 64]
for x, t, r in zip(xs, ['j²r', 'jr', 'j²r'], ['sujet', 'autre', 'resultat']):
    box(ax, x, 22, 22, 11, role=r, label=t)
for i, l in enumerate(['τ', 'σ']):
    arrow(ax, (xs[i] + 22.8, 27.5), (xs[i + 1] - 0.8, 27.5), 'varie')
    text(ax, xs[i] + 27.1, 31.5, l, 'varie', 's')
arrow(ax, (75, 34.2), (13, 34.2), 'resultat', curve=0.35)
text(ax, 44, 51.5, 'même nombre : fixé', 'resultat', 's')
text(ax, 44, 14, 'τ : j² ↦ j, r ↦ r  donne  j·r', 'encre', 's')
text(ax, 44, 8, 'σ : j ↦ j, r ↦ jr  donne  j·jr = j²r', 'encre', 's')
text(ax, 44, 2.5, 'Inv⟨στ⟩ = ℚ(j²r)', 'resultat', 'm', weight='bold')
save(fig, '63-150')
