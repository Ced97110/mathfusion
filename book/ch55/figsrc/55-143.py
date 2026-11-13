import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# x^2 - 5x + 6 = (x-2)(x-3): a = 1, b = -5, c = 6
a, b, c, r1, r2 = 1, -5, 6, 2, 3
assert (r1 + r2, r1 * r2) == (-b / a, c / a) and (r1 - r2) ** 2 == b * b - 4 * a * c == 1
box(ax, 3, 28, 24, 16, 'sujet', label=None)
text(ax, 15, 38, 'racines', 'sujet', 'm')
text(ax, 15, 32.5, '2 et 3', 'sujet', 'm', weight='bold')
labels = [r'$(x-2)(x-3)=x^2-5x+6$',
          r'somme $5=-b/a$, produit $6=c/a$',
          r'$(2-3)^2=1=b^2-4ac$']
heads = ['coefficients', 'somme et produit', 'discriminant']
for k, (lab, head) in enumerate(zip(labels, heads)):
    yy = 56 - k * 20
    text(ax, 33, yy + 11.5, head, 'fixe', 's', ha='left')
    box(ax, 33, yy, 52, 9, 'resultat', label=lab, size='s')
    arrow(ax, (27, 36), (33, yy + 4.5), 'varie')
save(fig, '55-143')
