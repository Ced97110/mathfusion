// Copyright: Your Name. Apache 2.0
// Edges drawn as thin lit tubes (1 px GL lines look cheap and ignore light).
import * as THREE from 'three';
import { EDGES } from './world.js';

const UNIT = new THREE.CylinderGeometry(1, 1, 1, 12, 1, false);
const UP = new THREE.Vector3(0, 1, 0);

export class EdgeTubes {
  constructor(material, radius, count = EDGES.length) {
    this.group = new THREE.Group();
    this.radius = radius;
    this.meshes = Array.from({ length: count }, () => {
      const m = new THREE.Mesh(UNIT, material);
      m.castShadow = true;
      this.group.add(m);
      return m;
    });
    this._d = new THREE.Vector3();
  }

  /** pts: vertices; pairs: list of [i, j] (default: the 12 edges of a parallelepiped). */
  update(pts, pairs = EDGES) {
    pairs.forEach(([i, j], k) => {
      const m = this.meshes[k];
      this._d.subVectors(pts[j], pts[i]);
      const len = this._d.length();
      m.position.addVectors(pts[i], pts[j]).multiplyScalar(0.5);
      m.quaternion.setFromUnitVectors(UP, this._d.multiplyScalar(1 / len));
      m.scale.set(this.radius, len, this.radius);
    });
  }
}
