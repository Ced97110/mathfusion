"""New figures for the rewritten chapter 41 (Fig. 41.A to 41.L). Zero tokens.

Usage (from the repo root): python3 tools/reecriture/fig41.py
Writes book/reecriture/ch41/fig/r41_X.svg and .png. Colours are those of the book's own figures
(blue = object defined, orange = what changes, grey = what does not, green = result, violet = second object).
Only the numbers of the text are drawn.
"""
from __future__ import annotations

import math
import re
from pathlib import Path

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, FancyArrowPatch, Polygon, Rectangle

OUT = Path(__file__).resolve().parents[2] / 'book' / 'reecriture' / 'ch41' / 'fig'
BLEU, ORANGE, VERT, GRIS, VIOLET = '#2a6fdb', '#e07b00', '#2a9d4b', '#777777', '#7b4fc9'
FS = 13
plt.rcParams.update({'font.family': 'DejaVu Sans', 'svg.fonttype': 'path', 'svg.hashsalt': 'fig41'})  # stable ids


def canvas(w: float, h: float) -> plt.Axes:
    fig = plt.figure(figsize=(w, h))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_aspect('equal')
    ax.axis('off')
    return ax


def arrow(ax: plt.Axes, p: tuple[float, float], q: tuple[float, float], color: str, lw: float = 3.0,
          dash: bool = False) -> None:
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle='-|>', mutation_scale=18, color=color, lw=lw,
                                 linestyle=(0, (4, 3)) if dash else '-', shrinkA=0, shrinkB=0))


def arc(ax: plt.Axes, c: tuple[float, float], r: float, a0: float, a1: float, color: str = GRIS,
        dash: bool = False) -> None:
    ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=a0, theta2=a1, color=color, lw=1.8,
                     linestyle=(0, (3, 2)) if dash else '-'))


def polar(r: float, deg: float, o: tuple[float, float] = (0, 0)) -> tuple[float, float]:
    return o[0] + r * math.cos(math.radians(deg)), o[1] + r * math.sin(math.radians(deg))


def right_angle(ax: plt.Axes, o: tuple[float, float], u: tuple[float, float], v: tuple[float, float],
                s: float = 0.18) -> None:
    """Small square at o between unit directions u and v."""
    pts = [(o[0] + s * u[0], o[1] + s * u[1]), (o[0] + s * (u[0] + v[0]), o[1] + s * (u[1] + v[1])),
           (o[0] + s * v[0], o[1] + s * v[1])]
    ax.plot(*zip(*pts), color=GRIS, lw=1.3)


def save(ax: plt.Axes, name: str, xlim: tuple[float, float], ylim: tuple[float, float]) -> None:
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    OUT.mkdir(parents=True, exist_ok=True)
    ax.figure.savefig(OUT / f'{name}.svg', transparent=False, facecolor='white', metadata={'Date': None})
    svg = (OUT / f'{name}.svg').read_text(encoding='utf8')  # drop the DOCTYPE: web hosts refuse DTDs in SVG
    (OUT / f'{name}.svg').write_text(re.sub(r'<!DOCTYPE[^>]*>\s*', '', svg), encoding='utf8')
    ax.figure.savefig(OUT / f'{name}.png', dpi=110, facecolor='white')
    plt.close(ax.figure)


def rot_arc(ax: plt.Axes, r: float, a0: float, a1: float, color: str, o: tuple[float, float] = (0, 0)) -> None:
    """Arc from a0 to a1 degrees (counterclockwise) with an arrowhead at a1: the turn."""
    pts = [polar(r, a0 + (a1 - a0) * t / 60, o) for t in range(61)]
    ax.plot(*zip(*pts[:-3]), color=color, lw=2.0)
    ax.add_patch(FancyArrowPatch(pts[-4], pts[-1], arrowstyle='-|>', mutation_scale=14, color=color, lw=2.0,
                                 shrinkA=0, shrinkB=0))


def fig_0() -> None:
    """An angle is a turn: full turn 360, half turn 180, quarter turn 90 (right angle), 60 = two thirds of 90."""
    ax = canvas(10.0, 3.0)
    gap = 3.0
    panels = [(360, 'un tour', '360°'), (180, 'un demi-tour', '180°'),
              (90, 'un quart de tour', '90° : un angle droit'), (60, 'deux tiers d’un', 'quart de tour : 60°')]
    for i, (deg, l1, l2) in enumerate(panels):
        o = (i * gap, 0)
        ax.plot(*zip(o, polar(1.0, 0, o)), color=GRIS, lw=2.4)  # start: looking east
        if deg == 360:
            pts = [polar(0.55, 3 + 350 * t / 80, o) for t in range(81)]
            ax.plot(*zip(*pts[:-3]), color=ORANGE, lw=2.0)
            ax.add_patch(FancyArrowPatch(pts[-4], pts[-1], arrowstyle='-|>', mutation_scale=14, color=ORANGE,
                                         lw=2.0, shrinkA=0, shrinkB=0))
        else:
            if deg == 60:
                ax.plot(*zip(o, polar(1.0, 90, o)), color=GRIS, lw=1.2, linestyle=(0, (3, 2)))
                arc(ax, o, 0.75, 0, 90, dash=True)
                for t in (30, 60):
                    ax.plot(*zip(polar(0.66, t, o), polar(0.84, t, o)), color=GRIS, lw=1.6)
            ax.plot(*zip(o, polar(1.0, deg, o)), color=ORANGE, lw=2.4)
            rot_arc(ax, 0.5, 0, deg, ORANGE, o)
            if deg == 90:
                right_angle(ax, o, (1, 0), (0, 1), 0.16)
        ax.plot([o[0]], [o[1]], 'o', color='black', ms=4)
        ax.text(o[0] + 0.1, -1.05, l1, fontsize=FS - 1, ha='center', va='top')
        ax.text(o[0] + 0.1, -1.4, l2, fontsize=FS - 1, ha='center', va='top', color=ORANGE)
    save(ax, 'r41_0', (-1.2, 3 * gap + 1.4), (-1.85, 1.2))


def fig_a() -> None:
    """Plane eastward (180 km/h), wind at 60 degrees from east toward north (100 km/h)."""
    ax = canvas(6.0, 3.4)
    k = 1 / 60  # 60 km/h per unit
    arrow(ax, (0, 0), (3.9, 0), GRIS, lw=1.2)
    arrow(ax, (0, 0), (0, 2.95), GRIS, lw=1.2)
    ax.text(3.95, -0.05, 'est', fontsize=FS, color=GRIS, va='center')
    ax.text(0, 3.05, 'nord', fontsize=FS, color=GRIS, ha='center')
    arc(ax, (0, 0), 2.55, 0, 90, dash=True)
    ax.text(*polar(2.7, 85), '90° : un quart de tour', fontsize=FS - 2, color=GRIS, ha='left', va='bottom')
    for deg in (30, 60):  # the quarter turn cut in three equal parts: the wind stops at the second mark
        ax.plot(*zip(polar(2.42, deg), polar(2.68, deg)), color=GRIS, lw=1.6)
        ax.text(*polar(2.82, deg), f'{deg}°', fontsize=FS - 3, color=GRIS, ha='left', va='center')
    ax.plot(*zip(polar(1.95, 60), polar(2.42, 60)), color=ORANGE, lw=1.2, linestyle=(0, (1, 2)))
    arrow(ax, (0, 0), (180 * k, 0), BLEU)
    ax.text(1.5, -0.35, 'avion : 180 km/h', fontsize=FS, color=BLEU, ha='center', va='top')
    w = polar(100 * k, 60)
    arrow(ax, (0, 0), w, ORANGE)
    ax.text(w[0] + 0.12, w[1] + 0.02, 'vent\n100 km/h', fontsize=FS, color=ORANGE, va='center')
    arc(ax, (0, 0), 0.75, 0, 60)
    ax.text(*polar(0.95, 30), '60°', fontsize=FS, color=GRIS, ha='left', va='center')
    ax.plot([0], [0], 'o', color='black', ms=5)
    ax.text(-0.12, -0.12, 'O', fontsize=FS, ha='right', va='top', style='italic')
    save(ax, 'r41_A', (-0.6, 4.6), (-0.9, 3.4))


def fig_b() -> None:
    """Suitcase pulled by a 50 N force inclined 30 degrees above the ground."""
    ax = canvas(6.0, 3.0)
    ax.plot([-1.9, 4.2], [0, 0], color=GRIS, lw=1.5)
    ax.text(4.2, -0.12, 'sol', fontsize=FS - 1, color=GRIS, ha='right', va='top')
    ax.add_patch(Rectangle((-1.6, 0.02), 1.4, 1.0, fc='#eeeeee', ec=GRIS, lw=1.5))
    ax.text(-0.9, 0.5, 'valise', fontsize=FS - 1, color=GRIS, ha='center', va='center')
    p = (-0.2, 1.0)
    f = polar(3.0, 30, p)
    arrow(ax, p, (f[0], p[1]), VERT, lw=2.4, dash=True)
    ax.text((p[0] + f[0]) / 2, p[1] - 0.12, '? la part qui fait avancer', fontsize=FS - 1, color=VERT,
            ha='center', va='top')
    arrow(ax, (f[0], p[1]), f, GRIS, lw=1.6, dash=True)
    ax.text(f[0] + 0.1, (p[1] + f[1]) / 2, 'la part qui\ntire vers\nle haut', fontsize=FS - 2, color=GRIS,
            va='center')
    arrow(ax, p, f, BLEU)
    ax.text(*polar(1.7, 38, p), 'votre force : 50 N', fontsize=FS, color=BLEU, ha='right', va='bottom',
            rotation=30, rotation_mode='anchor')
    arc(ax, p, 0.9, 0, 30)
    ax.text(*polar(1.05, 13, p), '30°', fontsize=FS, color=GRIS, va='center')
    save(ax, 'r41_B', (-2.0, 4.8), (-0.6, 2.7))


def fig_c() -> None:
    """The four quadrants of the frame, with the signs of the two components."""
    ax = canvas(6.0, 4.4)
    arrow(ax, (-2.9, 0), (2.9, 0), GRIS, lw=1.2)
    arrow(ax, (0, -2.0), (0, 2.1), GRIS, lw=1.2)
    ax.text(2.95, 0, 'x (est)', fontsize=FS - 1, color=GRIS, va='center')
    ax.text(0, 2.2, 'y (nord)', fontsize=FS - 1, color=GRIS, ha='center')
    quads = [((1.45, 1.0), '1er quadrant', 'est et nord', 'a positif, b positif'),
             ((-1.45, 1.0), '2e quadrant', 'ouest et nord', 'a négatif, b positif'),
             ((-1.45, -1.0), '3e quadrant', 'ouest et sud', 'a négatif, b négatif'),
             ((1.45, -1.0), '4e quadrant', 'est et sud', 'a positif, b négatif')]
    for (x, y), name, side, signs in quads:
        ax.text(x, y + 0.35, name, fontsize=FS, ha='center', weight='bold')
        ax.text(x, y, side, fontsize=FS - 1, ha='center', color=GRIS)
        ax.text(x, y - 0.35, signs, fontsize=FS - 1, ha='center', color=GRIS)
    ax.text(-0.1, -0.1, 'O', fontsize=FS, ha='right', va='top', style='italic')
    save(ax, 'r41_C', (-3.2, 3.9), (-2.2, 2.6))


def iso(x: float, y: float, z: float) -> tuple[float, float]:
    """Exact isometric projection."""
    c = math.cos(math.radians(30))
    return (x + y) * c, (y - x) * 0.5 + z


def fig_d() -> None:
    """Box a x b x c: floor diagonal, then the arrow from corner to opposite corner."""
    ax = canvas(5.6, 4.6)
    a, b, c = 3.0, 2.0, 1.6
    corners = {(i, j, k): iso(i * a, j * b, k * c) for i in (0, 1) for j in (0, 1) for k in (0, 1)}
    hidden = {(0, 1, 0)}  # the corner farthest from the viewer: its three edges are hidden, drawn dashed
    for p in corners:
        for d in range(3):
            if p[d] == 0:
                q = tuple(1 if e == d else p[e] for e in range(3))
                dash = (0, (3, 2)) if p in hidden or q in hidden else '-'
                ax.plot(*zip(corners[p], corners[q]), color=GRIS, lw=1.2, linestyle=dash)
    ax.add_patch(Polygon([corners[(0, 0, 0)], corners[(1, 0, 0)], corners[(1, 1, 0)], corners[(0, 1, 0)]],
                         closed=True, fc='#eef3fb', ec='none', zorder=0))
    o, floor, top = corners[(0, 0, 0)], corners[(1, 1, 0)], corners[(1, 1, 1)]
    ax.plot(*zip(o, floor), color=ORANGE, lw=2.6)
    ax.plot(*zip(floor, top), color=GRIS, lw=2.6)
    arrow(ax, o, top, BLEU)
    # right angles: between a and b at the origin, between the diagonal and c at the floor corner
    ux, uy = [(e1 - e0) / a for e0, e1 in zip(o, corners[(1, 0, 0)])], [(e1 - e0) / b for e0, e1 in zip(o, corners[(0, 1, 0)])]
    right_angle(ax, o, tuple(ux), tuple(uy), 0.3)
    dl = math.dist(o, floor)
    ud = ((o[0] - floor[0]) / dl, (o[1] - floor[1]) / dl)
    right_angle(ax, floor, ud, (0, 1), 0.22)
    def mid(p, q):
        return ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    ax.text(*mid(o, corners[(1, 0, 0)]), 'a  ', fontsize=FS + 1, ha='right', va='top', style='italic')
    ax.text(*mid(o, corners[(0, 1, 0)]), 'b  ', fontsize=FS + 1, ha='right', va='bottom', style='italic')
    ax.text(floor[0] + 0.12, (floor[1] + top[1]) / 2, 'c', fontsize=FS + 1, color=GRIS, style='italic',
            va='center')
    m = mid(o, floor)
    ax.text(m[0], m[1] - 0.15, '√(a² + b²)', fontsize=FS, color=ORANGE, ha='center', va='top')
    t = mid(o, top)
    ax.text(t[0] - 0.12, t[1] + 0.08, 'v', fontsize=FS + 2, color=BLEU, weight='bold', ha='right')
    ax.text(o[0] - 0.15, o[1], 'O', fontsize=FS, ha='right', va='center', style='italic')
    xs = [p[0] for p in corners.values()]
    ys = [p[1] for p in corners.values()]
    save(ax, 'r41_D', (min(xs) - 0.7, max(xs) + 0.7), (min(ys) - 0.7, max(ys) + 0.4))


def fig_e() -> None:
    """Two ropes: 60 N at 40 degrees east of north, 70 N at 40 degrees west of north."""
    ax = canvas(6.0, 4.2)
    k = 1 / 30
    arrow(ax, (-2.9, 0), (2.9, 0), GRIS, lw=1.2)
    arrow(ax, (0, 0), (0, 2.9), GRIS, lw=1.2)
    ax.text(2.95, 0, 'est', fontsize=FS - 1, color=GRIS, va='center')
    ax.text(-2.95, 0, 'ouest', fontsize=FS - 1, color=GRIS, va='center', ha='right')
    ax.text(0, 3.0, 'nord', fontsize=FS - 1, color=GRIS, ha='center')
    f1, f2 = polar(60 * k, 50), polar(70 * k, 130)
    arrow(ax, (0, 0), f1, BLEU)
    arrow(ax, (0, 0), f2, VIOLET)
    ax.text(f1[0] + 0.08, f1[1], 'F₁ : 60 N', fontsize=FS, color=BLEU, va='bottom')
    ax.text(f2[0] - 0.08, f2[1], 'F₂ : 70 N', fontsize=FS, color=VIOLET, va='bottom', ha='right')
    arc(ax, (0, 0), 1.25, 50, 90)
    arc(ax, (0, 0), 1.25, 90, 130)
    ax.text(*polar(1.42, 70), '40°', fontsize=FS - 1, color=GRIS, ha='center', va='center')
    ax.text(*polar(1.42, 110), '40°', fontsize=FS - 1, color=GRIS, ha='center', va='center')
    arc(ax, (0, 0), 0.55, 0, 50, dash=True)
    ax.text(*polar(0.75, 22), '50°', fontsize=FS - 2, color=GRIS, ha='left', va='center')
    arc(ax, (0, 0), 0.38, 0, 130, dash=True)
    ax.text(*polar(0.62, 160), '130°', fontsize=FS - 2, color=GRIS, ha='right', va='center')
    ax.plot([0], [0], 'o', color='black', ms=5)
    ax.text(0.1, -0.12, 'O', fontsize=FS, va='top', style='italic')
    save(ax, 'r41_E', (-3.6, 3.6), (-0.5, 3.3))


def fig_f() -> None:
    """Number axis: start at 5, go back 8, arrive at -3."""
    ax = canvas(6.4, 1.9)
    arrow(ax, (-6.6, 0), (6.6, 0), GRIS, lw=1.2)
    for n in range(-6, 7):
        ax.plot([n, n], [-0.1, 0.1], color=GRIS, lw=1.2)
        ax.text(n, -0.22, str(n).replace('-', '−'), fontsize=FS - 2, ha='center', va='top',
                color='black' if n == 0 else GRIS)
    ax.add_patch(FancyArrowPatch((5, 0.12), (-3, 0.12), connectionstyle='arc3,rad=0.25', arrowstyle='-|>',
                                 mutation_scale=16, color=ORANGE, lw=2.2, shrinkA=0, shrinkB=0))
    ax.text(1, 1.25, 'reculer de 8', fontsize=FS - 1, color=ORANGE, ha='center')
    ax.plot([5], [0], 'o', color=GRIS, ms=7)
    ax.plot([-3], [0], 'o', color=VERT, ms=8)
    ax.text(-3, -0.62, 'arrivée : −3', fontsize=FS - 1, color=VERT, ha='center', va='top')
    ax.text(5, -0.62, 'départ : 5', fontsize=FS - 1, color=GRIS, ha='center', va='top')
    ax.text(-6.4, 0.35, '← nombres négatifs', fontsize=FS - 2, color=GRIS, ha='left')
    ax.text(6.4, 0.35, 'nombres positifs →', fontsize=FS - 2, color=GRIS, ha='right')
    save(ax, 'r41_F', (-7.0, 7.0), (-1.1, 1.6))


def fig_g() -> None:
    """Circle of radius 1: the points at 60 and 120 degrees; their x-coordinates are 0.5 and -0.5."""
    ax = canvas(5.6, 3.9)
    arrow(ax, (-1.55, 0), (1.6, 0), GRIS, lw=1.2)
    arrow(ax, (0, -0.25), (0, 1.45), GRIS, lw=1.2)
    ax.text(1.63, 0, 'x (est)', fontsize=FS - 2, color=GRIS, va='center')
    ax.text(0, 1.5, 'y (nord)', fontsize=FS - 2, color=GRIS, ha='center')
    ax.add_patch(Arc((0, 0), 2, 2, theta1=0, theta2=180, color=GRIS, lw=1.2))
    for deg, col in ((60, BLEU), (120, VIOLET)):
        p = polar(1, deg)
        ax.plot([0, p[0]], [0, p[1]], color=col, lw=2.2)
        ax.plot([p[0], p[0]], [0, p[1]], color=col, lw=1.3, linestyle=(0, (3, 2)))
        ax.plot([p[0]], [p[1]], 'o', color=col, ms=6)
        ax.plot([p[0]], [0], 'o', color=VERT, ms=6)
    ax.text(0.5, -0.24, 'cos 60° = 0,5', fontsize=FS - 2, color=VERT, ha='center', va='top')
    ax.text(-0.5, -0.24, 'cos 120° = −0,5', fontsize=FS - 2, color=VERT, ha='center', va='top')
    ax.text(*polar(1.08, 60), '60°', fontsize=FS - 1, color=BLEU, ha='left', va='bottom')
    ax.text(*polar(1.08, 120), '120°', fontsize=FS - 1, color=VIOLET, ha='right', va='bottom')
    arc(ax, (0, 0), 0.22, 0, 60, color=BLEU)
    arc(ax, (0, 0), 0.34, 0, 120, color=VIOLET)
    r1 = polar(0.62, 60)
    ax.text(r1[0] - 0.07, r1[1] + 0.02, '1', fontsize=FS - 1, color=BLEU, ha='right', va='bottom')
    ax.text(-0.04, -0.04, 'O', fontsize=FS - 1, ha='right', va='top', style='italic')
    save(ax, 'r41_G', (-1.75, 2.15), (-0.6, 1.65))


def fig_h() -> None:
    """Vector from A(5, 7) to B(18, 13): the two gaps 13 and 6."""
    ax = canvas(6.0, 3.8)
    k = 0.25
    arrow(ax, (0, 0), (21 * k, 0), GRIS, lw=1.2)
    arrow(ax, (0, 0), (0, 15.5 * k), GRIS, lw=1.2)
    ax.text(21.2 * k, 0, 'x', fontsize=FS, color=GRIS, va='center', style='italic')
    ax.text(0, 15.8 * k, 'y', fontsize=FS, color=GRIS, ha='center', style='italic')
    a, b = (5 * k, 7 * k), (18 * k, 13 * k)
    for x in (5, 18):
        ax.plot([x * k, x * k], [0, (7 if x == 5 else 13) * k], color=GRIS, lw=0.8, linestyle=(0, (2, 3)))
        ax.text(x * k, -0.12, str(x), fontsize=FS - 1, color=GRIS, ha='center', va='top')
    for y, x in ((7, 5), (13, 18)):
        ax.plot([0, x * k], [y * k, y * k], color=GRIS, lw=0.8, linestyle=(0, (2, 3)))
        ax.text(-0.1, y * k, str(y), fontsize=FS - 1, color=GRIS, ha='right', va='center')
    arrow(ax, a, (b[0], a[1]), ORANGE, lw=2.0, dash=True)
    arrow(ax, (b[0], a[1]), b, ORANGE, lw=2.0, dash=True)
    ax.text((a[0] + b[0]) / 2, a[1] - 0.1, '18 − 5 = 13', fontsize=FS - 1, color=ORANGE, ha='center', va='top')
    ax.text(b[0] + 0.1, (a[1] + b[1]) / 2, '13 − 7 = 6', fontsize=FS - 1, color=ORANGE, va='center')
    arrow(ax, a, b, BLEU)
    ax.plot(*a, 'o', color='black', ms=5)
    ax.plot(*b, 'o', color='black', ms=5)
    ax.text(a[0] - 0.1, a[1] + 0.08, 'A(5, 7)', fontsize=FS, ha='right', va='bottom')
    ax.text(b[0] - 0.1, b[1] + 0.1, 'B(18, 13)', fontsize=FS, ha='right', va='bottom')
    ax.text(-0.08, -0.08, 'O', fontsize=FS - 1, ha='right', va='top', style='italic')
    save(ax, 'r41_H', (-0.7, 6.3), (-0.5, 4.2))


def iso_back(x: float, y: float, z: float) -> tuple[float, float]:
    """Exact isometric projection seen from direction (-1, 1, 1). For Fig. 41.I the view of iso() puts the
    tip of v on an edge of the box, and the view from (-1, -1, 1) puts w on its own height."""
    c = math.cos(math.radians(30))
    return -(x + y) * c, (x - y) * 0.5 + z


def fig_i() -> None:
    """Parallelepiped on u = <2,0,0>, v = <1,2,0>, w = <1,1,3>; base on u and v, height of w above it."""
    ax = canvas(5.0, 5.0)
    vec = [(2.0, 0.0, 0.0), (1.0, 2.0, 0.0), (1.0, 1.0, 3.0)]
    view = (-1.0, 1.0, 1.0)  # toward the viewer
    def dot(p, q):
        return sum(a * b for a, b in zip(p, q))
    def cross(p, q):
        return (p[1] * q[2] - p[2] * q[1], p[2] * q[0] - p[0] * q[2], p[0] * q[1] - p[1] * q[0])
    back = set()  # faces (i, side) turned away from the viewer; face i is spanned by the two other vectors
    for i in range(3):
        a_, b_ = [vec[j] for j in range(3) if j != i]
        n = cross(a_, b_)
        if dot(n, vec[i]) > 0:
            n = tuple(-c for c in n)  # outward normal of the face through the origin
        back.add((i, 0) if dot(n, view) < 0 else (i, 1))
    def pt(s):
        return tuple(sum(vec[j][e] for j in range(3) if s[j]) for e in range(3))
    def P(s):
        return iso_back(*pt(s))
    for s in [(i, j, k) for i in (0, 1) for j in (0, 1) for k in (0, 1)]:
        for d in range(3):
            if s[d] == 0 and s != (0, 0, 0):  # the three edges at O are the arrows
                t = tuple(1 if e == d else s[e] for e in range(3))
                hidden = all((e, s[e]) in back for e in range(3) if e != d)
                ax.plot(*zip(P(s), P(t)), color=GRIS, lw=1.1, linestyle=(0, (3, 2)) if hidden else '-')
    ax.add_patch(Polygon([P(s) for s in ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0))], closed=True,
                         fc='#dde8f8', ec='none', zorder=0))
    o = P((0, 0, 0))
    def at_o(d):
        return all((e, 0) in back for e in range(3) if e != d)  # arrow hidden behind the box
    arrow(ax, o, P((1, 0, 0)), BLEU, dash=at_o(0))
    arrow(ax, o, P((0, 1, 0)), ORANGE, dash=at_o(1))
    arrow(ax, o, P((0, 0, 1)), VIOLET, dash=at_o(2))
    # the height, drawn from a point inside the top face straight down to the base (from the tip of w,
    # it would lie on the arrow u in this view)
    top, foot = iso_back(2.0, 1.4, 3.0), iso_back(2.0, 1.4, 0.0)
    ax.plot(*zip(top, foot), color=GRIS, lw=1.8, linestyle=(0, (4, 3)))
    ax.plot([foot[0]], [foot[1]], 'o', color=GRIS, ms=4)
    ax.text(foot[0] - 0.1, (top[1] + foot[1]) / 2 + 0.3, 'hauteur', fontsize=FS - 1, color=GRIS, va='center', ha='right')
    ax.text(*iso_back(1.1, -0.3, 0), 'u', fontsize=FS + 2, color=BLEU, weight='bold', ha='left', va='top')
    ax.text(*iso_back(0.2, 1.0, 0), 'v', fontsize=FS + 2, color=ORANGE, weight='bold', ha='right', va='top')
    ax.text(*iso_back(0.45, 0.3, 1.7), 'w', fontsize=FS + 2, color=VIOLET, weight='bold', ha='right')
    c = iso_back(2.0, 0.9, 0)
    ax.text(c[0], c[1], 'base', fontsize=FS - 1, color=BLEU, ha='center', va='center')
    ax.text(o[0], o[1] - 0.12, 'O', fontsize=FS, ha='center', va='top', style='italic')
    pts = [P((i, j, k)) for i in (0, 1) for j in (0, 1) for k in (0, 1)]
    save(ax, 'r41_I', (min(p[0] for p in pts) - 0.6, max(p[0] for p in pts) + 0.6),
         (min(p[1] for p in pts) - 0.5, max(p[1] for p in pts) + 0.3))


def fig_j() -> None:
    """Effect 1 check: triangle O, tip of a, tip of r; outer angle 60 degrees, inner angle 120 degrees."""
    ax = canvas(6.4, 2.9)
    k = 1 / 60
    t = (180 * k, 0)
    r = polar(100 * k, 60, t)
    ax.plot([t[0], t[0] + 1.3], [0, 0], color=GRIS, lw=1.2, linestyle=(0, (3, 2)))
    ax.text(t[0] + 1.35, 0, 'a prolongée', fontsize=FS - 3, color=GRIS, va='center')
    arrow(ax, (0, 0), t, BLEU)
    ax.text(1.5, -0.12, 'a : 180', fontsize=FS, color=BLEU, ha='center', va='top')
    arrow(ax, t, r, ORANGE)
    ax.text(r[0] + 0.1, (r[1] + 0) / 2 + 0.3, 'v : 100', fontsize=FS, color=ORANGE, va='center')
    arrow(ax, (0, 0), r, VERT)
    ax.text(1.65, 0.95, 'r', fontsize=FS + 2, color=VERT, weight='bold', ha='right')
    arc(ax, t, 0.5, 0, 60)
    ax.text(*polar(0.65, 25, t), '60°', fontsize=FS - 1, color=GRIS, va='center')
    arc(ax, t, 0.32, 60, 180, color=VERT)
    ax.text(*polar(0.45, 135, t), '120°', fontsize=FS - 1, color=VERT, ha='right', va='bottom')
    ax.plot([0], [0], 'o', color='black', ms=5)
    ax.text(-0.1, -0.1, 'O', fontsize=FS, ha='right', va='top', style='italic')
    ax.text(t[0], -0.12, 'bout de a', fontsize=FS - 2, ha='center', va='top')
    ax.text(r[0], r[1] + 0.08, 'bout de r', fontsize=FS - 2, ha='center', va='bottom')
    save(ax, 'r41_J', (-0.5, 5.5), (-0.6, 1.9))


def fig_k() -> None:
    """Effect 2: the true direction 93.69 degrees and the arctangent answer -86.31 degrees, a half-turn apart."""
    ax = canvas(5.6, 4.4)
    arrow(ax, (-2.2, 0), (2.4, 0), GRIS, lw=1.2)
    arrow(ax, (0, -2.2), (0, 2.4), GRIS, lw=1.2)
    ax.text(2.45, 0, 'est', fontsize=FS - 2, color=GRIS, va='center')
    ax.text(-2.25, 0, 'ouest', fontsize=FS - 2, color=GRIS, va='center', ha='right')
    ax.text(0, 2.45, 'nord', fontsize=FS - 2, color=GRIS, ha='center', va='bottom')
    ax.text(0, -2.25, 'sud', fontsize=FS - 2, color=GRIS, ha='center', va='top')
    good, bad = polar(1.9, 93.69), polar(1.9, -86.31)
    arrow(ax, (0, 0), good, VERT)
    arrow(ax, (0, 0), bad, '#d1342f', lw=2.4, dash=True)
    ax.text(good[0] - 0.1, good[1], 'F₁ + F₂\n93,69°', fontsize=FS - 1, color=VERT, ha='right', va='top')
    ax.text(bad[0] + 0.12, bad[1] + 0.1, 'réponse de arctan :\n−86,31°', fontsize=FS - 2, color='#d1342f',
            va='bottom')
    arc(ax, (0, 0), 1.0, -86.31, 93.69, color=ORANGE)
    ax.text(1.05, 0.25, '+180° :\nun demi-tour', fontsize=FS - 2, color=ORANGE, va='bottom')
    ax.text(-0.08, -0.08, 'O', fontsize=FS - 1, ha='right', va='top', style='italic')
    save(ax, 'r41_K', (-2.9, 3.4), (-2.6, 2.75))


def fig_l() -> None:
    """Carrying a bag at constant height: force upward, displacement horizontal, right angle."""
    ax = canvas(6.0, 2.6)
    ax.plot([-0.3, 5.3], [0, 0], color=GRIS, lw=1.2)
    ax.text(5.3, -0.1, 'sol', fontsize=FS - 2, color=GRIS, ha='right', va='top')
    ax.add_patch(Rectangle((0.2, 0.9), 0.8, 0.6, fc='#eeeeee', ec=GRIS, lw=1.3))
    ax.text(0.6, 1.2, 'sac', fontsize=FS - 2, color=GRIS, ha='center', va='center')
    p = (1.0, 1.2)
    arrow(ax, p, (4.2, 1.2), ORANGE, dash=True)
    ax.text(2.6, 1.08, 'le sac avance à hauteur constante', fontsize=FS - 2, color=ORANGE, ha='center', va='top')
    arrow(ax, p, (1.0, 2.4), BLEU)
    ax.text(1.15, 2.15, 'votre bras pousse vers le haut', fontsize=FS - 2, color=BLEU, va='center')
    right_angle(ax, p, (0, 1), (1, 0), 0.18)
    save(ax, 'r41_L', (-0.4, 5.5), (-0.4, 2.7))


if __name__ == '__main__':
    for f in (fig_0, fig_a, fig_b, fig_c, fig_d, fig_e, fig_f, fig_g, fig_h, fig_i, fig_j, fig_k, fig_l):
        f()
    print('figures :', sorted(p.name for p in OUT.glob('*.svg')))
