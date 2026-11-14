# Copyright: Your Name. Apache 2.0
"""Scene of fiche 41-123: flat parallelogram, right box ("carton"), parallelepiped of u, v, w.

Exact geometry from the fiche numbers only. Writes scene.json for render2.py and the
expected pixel position of every vertex and label anchor, for check2.py and the overlay.
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import numpy as np

U, V, W = np.array([2.0, 0, 0]), np.array([1.0, 2, 0]), np.array([1.0, 1, 3])
AZ, EL = np.radians(330.0), np.radians(25.0)  # w tilted 28° on screen (see degen.py)
RES_X, RES_Y = 2400, 1200
GAP = 5.0  # world units between object centres, along the screen x axis

ROLE = {  # figstyle COL / FILL
    "fixe": ("#5f6773", "#eceef1"),
    "autre": ("#6b3fa0", "#e6dcf2"),
    "sujet": ("#1f4e79", "#d6e4f2"),
}


def rgb(h: str) -> list[float]:
    return [int(h[i : i + 2], 16) / 255 for i in (1, 3, 5)]


def box(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> tuple[np.ndarray, list[list[int]]]:
    pts = np.array([i * a + j * b + k * c for k, j, i in itertools.product((0, 1), repeat=3)])
    faces = [[0, 2, 3, 1], [4, 5, 7, 6], [0, 1, 5, 4], [2, 6, 7, 3], [0, 4, 6, 2], [1, 3, 7, 5]]
    return pts, faces


def frame() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    z = np.array([np.cos(EL) * np.cos(AZ), np.cos(EL) * np.sin(AZ), np.sin(EL)])
    x = np.cross([0.0, 0.0, 1.0], z)
    x /= np.linalg.norm(x)
    return x, np.cross(z, x), z


def main(out: Path) -> None:
    x, y, z = frame()
    floor_x = np.array([x[0], x[1], 0.0]) / np.linalg.norm(x[:2])
    plate = (np.array([[0, 0, 0], U, U + V, V], float), [[0, 1, 2, 3]])
    shapes = [("parallelogramme", "fixe", plate), ("carton", "autre", box(np.array([2.0, 0, 0]), np.array([0, 2.0, 0]), np.array([0, 0, 3.0])))]
    shapes.append(("parallelepipede", "sujet", box(U, V, W)))
    objs = []
    for k, (name, role, (pts, faces)) in enumerate(shapes):
        centre = pts.mean(axis=0) * [1, 1, 0]
        offset = (k - 1) * GAP * floor_x - centre
        objs.append({"name": name, "role": role, "vertices": (pts + offset).tolist(), "faces": faces,
                     "edge": rgb(ROLE[role][0]), "face": rgb(ROLE[role][1])})
    allpts = np.vstack([o["vertices"] for o in objs])
    mid = (allpts.min(0) + allpts.max(0)) / 2
    loc = mid + 30 * z
    rot = np.column_stack([x, y, z])
    xy = (allpts - loc) @ rot[:, :2]
    scale = 1.06 * max(np.ptp(xy[:, 0]), 2 * np.ptp(xy[:, 1]))  # ortho_scale spans the wider side (x)
    # parallelepiped: anchors for labels (edge midpoints of u, v, w and the height foot/top)
    o = np.array(objs[2]["vertices"][0])
    top = o + W + (U + V) / 2  # centre of the top face; its vertical foot lies inside the base
    anchors = {"u": o + U / 2, "v": o + V / 2, "w": o + W / 2, "h_top": top, "h_foot": top - np.array([0, 0, 3.0])}
    data = {"objects": objs, "anchors": {k: v.tolist() for k, v in anchors.items()},
            "camera": {"rot_columns": rot.T.tolist(), "location": loc.tolist(), "ortho_scale": scale, "res": [RES_X, RES_Y]}}
    out.write_text(json.dumps(data, indent=1))
    print("scene ->", out)


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("scene.json"))
