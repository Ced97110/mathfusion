import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
a, b, c = 40, 50, 60; s = 75
Ax = (c*c + a*a - b*b) / (2*a); A = (Ax, math.sqrt(c*c - Ax*Ax)); B = (0.0, 0.0); C = (40.0, 0.0)
ra = math.sqrt(s*(s-a)*(s-b)*(s-c))/(s-a); Ia = (s - c, -ra)
k, oy = 0.34, 14
xs = [4, 26, 48, 70]
items = [([A, B, Ia], 'sujet', '850,4', r'$ABI_a$'), ([A, Ia, C], 'autre', '708,7', r'$ACI_a$'),
         ([B, Ia, C], 'varie', '566,9', r'$BI_aC$'), ([A, B, C], 'resultat', '992,2', r'$ABC$')]
fig, ax = canvas(40)
for ox, (pts, role, num, name) in zip(xs, items):
    T = lambda p, ox=ox: (ox + k*p[0], oy + k*p[1])
    poly(ax, [T(A), T(B), T(Ia), T(C)], 'fixe')
    poly(ax, [T(p) for p in pts], role)
    text(ax, ox + 20*k, 35.5, num, role, 'm', weight='bold')
    text(ax, ox + 20*k, 1.8, name, role, 's')
for ox, op, role in zip(xs, ['+', '−', '='], ['encre', 'varie', 'encre']):
    text(ax, ox + 19.8, oy + 5, op, role, 'l', weight='bold')
save(fig, '37-076')
