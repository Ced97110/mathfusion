// Copyright: Your Name. Apache 2.0
// « Vent de travers » v2 — PROCHE scene: runway 09 lights in true size (edge lights every 60 m,
// threshold bar, approach lights over 900 m). The painted surface is in the ground shader.
// Glow = HDR emissive lamps picked up by the bloom of the rendering pipeline (no GlowLayer).
// All lamps are warm white: green and red are reserved for their meaning in the film.

import { PISTE_L, PISTE_W } from './proche-sol-glsl.js';

const B = globalThis.BABYLON;

/**
 * @param {BABYLON.Scene} scene
 * @param {{ ombres: BABYLON.CascadedShadowGenerator }} o
 */
export function creerFeux(scene, o) {
  const lampes = []; // [x, y, z]
  const pieds = []; // [x, z, height]
  const bord = PISTE_W / 2 + 1.5;
  for (let x = 0; x <= PISTE_L + 0.1; x += 60) {
    for (const z of [-bord, bord]) { lampes.push([x, 0.36, z]); pieds.push([x, z, 0.34]); }
  }
  for (let z = -PISTE_W / 2 + 1.5; z <= PISTE_W / 2 - 1.4; z += 3) { lampes.push([-1.5, 0.3, z]); pieds.push([-1.5, z, 0.28]); }
  for (let x = -30; x >= -900; x -= 30) {
    const h = 0.4 + (-x) * 0.004; // the line stays level while the ground does not slope (gentle rise)
    const n = x === -300 ? 15 : 5;
    for (let k = 0; k < n; k++) {
      const z = (k - (n - 1) / 2) * (x === -300 ? 1.6 : 1.05);
      lampes.push([x, h + 0.04, z]);
    }
    pieds.push([x, 0, h]);
  }

  const lampe = B.MeshBuilder.CreateSphere('lampe', { diameter: 0.16, segments: 8 }, scene);
  lampe.scaling.y = 0.7;
  lampe.bakeCurrentTransformIntoVertices();
  const matL = new B.StandardMaterial('matLampe', scene);
  matL.disableLighting = true;
  matL.emissiveColor = new B.Color3(1.0, 0.86, 0.62).scale(40);
  lampe.material = matL;
  const bl = new Float32Array(lampes.length * 16);
  lampes.forEach(([x, y, z], i) => B.Matrix.Translation(x, y, z).copyToArray(bl, i * 16));
  lampe.thinInstanceSetBuffer('matrix', bl, 16, true);

  const pied = B.MeshBuilder.CreateCylinder('piedFeu', { height: 1, diameter: 0.07, tessellation: 10 }, scene);
  pied.bakeTransformIntoVertices(B.Matrix.Translation(0, 0.5, 0));
  const matP = new B.PBRMaterial('matPied', scene);
  matP.albedoColor = new B.Color3(0.32, 0.32, 0.31);
  matP.metallic = 0.6; matP.roughness = 0.5;
  pied.material = matP;
  const bp = new Float32Array(pieds.length * 16);
  pieds.forEach(([x, z, h], i) => B.Matrix.Scaling(1, h, 1).multiply(B.Matrix.Translation(x, 0, z)).copyToArray(bp, i * 16));
  pied.thinInstanceSetBuffer('matrix', bp, 16, true);
  // approach light cross bars
  const barre = B.MeshBuilder.CreateBox('barreFeux', { width: 0.06, height: 0.06, depth: 1 }, scene);
  barre.material = matP;
  const bb = [];
  for (let x = -30; x >= -900; x -= 30) {
    const h = 0.4 + (-x) * 0.004;
    const L = x === -300 ? 23 : 4.4;
    bb.push(B.Matrix.Scaling(1, 1, L).multiply(B.Matrix.Translation(x, h, 0)));
  }
  const bbuf = new Float32Array(bb.length * 16);
  bb.forEach((m, i) => m.copyToArray(bbuf, i * 16));
  barre.thinInstanceSetBuffer('matrix', bbuf, 16, true);

  for (const m of [lampe, pied, barre]) { m.isPickable = false; m.receiveShadows = true; }
  o.ombres.addShadowCaster(pied);
  o.ombres.addShadowCaster(barre);

  /** @param {boolean} vis */
  function maj(vis) { for (const m of [lampe, pied, barre]) m.setEnabled(vis); }
  return { lampe, pied, barre, maj, emissifs: [lampe] };
}
