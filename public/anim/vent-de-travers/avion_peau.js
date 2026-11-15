// Copyright: Your Name. Apache 2.0
// Procedural surface detail of the Cessna (« Vent de travers », v2): skin atlas (paint, blue stripe,
// window cut-outs in alpha), normal maps (panel grooves, rivet domes) and the propeller blur disc.
// Everything is drawn once at build time with anti-aliased canvas strokes, then mip-mapped and
// sampled with 16x anisotropic filtering, so details stay smooth at every distance.

import { COULEUR } from './communs.js';
import { FUS, angleY, ouvertures, AILE } from './avion_formes.js';

const B = globalThis.BABYLON;

/* ------------------------------------------------------------------ canvas helpers */

function toile(w, h) {
  if (typeof OffscreenCanvas !== 'undefined') return new OffscreenCanvas(w, h);
  const c = document.createElement('canvas');
  c.width = w; c.height = h;
  return c;
}

/** Dynamic texture with mip-maps and anisotropic filtering; its canvas is drawn by dessiner(ctx). */
function texture(scene, nom, w, h, dessiner) {
  const tx = new B.DynamicTexture(nom, { width: w, height: h }, scene, true, B.Texture.TRILINEAR_SAMPLINGMODE);
  dessiner(tx.getContext());
  tx.anisotropicFilteringLevel = 16;
  tx.wrapU = B.Texture.CLAMP_ADDRESSMODE;
  tx.wrapV = B.Texture.WRAP_ADDRESSMODE;
  tx.update(true);
  return tx;
}

/**
 * Tangent-space normal map from a height canvas (grey level = height).
 * A 3x3 blur removes 8-bit steps; v wraps when wrapV (fuselage circumference).
 */
function normales(ctxH, w, h, force, wrapV) {
  const src = ctxH.getImageData(0, 0, w, h).data;
  let hgt = new Float32Array(w * h);
  for (let i = 0; i < w * h; i++) hgt[i] = src[4 * i] / 255;
  const tmp = new Float32Array(w * h);
  const ligne = (y) => (wrapV ? (y + h) % h : Math.min(h - 1, Math.max(0, y)));
  for (let y = 0; y < h; y++) {
    for (let x = 0; x < w; x++) {
      const a = Math.max(0, x - 1), b = Math.min(w - 1, x + 1);
      tmp[y * w + x] = (hgt[y * w + a] + hgt[y * w + x] + hgt[y * w + b]) / 3;
    }
  }
  for (let y = 0; y < h; y++) {
    const y0 = ligne(y - 1), y1 = ligne(y + 1);
    for (let x = 0; x < w; x++) hgt[y * w + x] = (tmp[y0 * w + x] + tmp[y * w + x] + tmp[y1 * w + x]) / 3;
  }
  const out = new ImageData(w, h);
  const o = out.data;
  for (let y = 0; y < h; y++) {
    const y0 = ligne(y - 1), y1 = ligne(y + 1);
    for (let x = 0; x < w; x++) {
      const xa = Math.max(0, x - 1), xb = Math.min(w - 1, x + 1);
      const nx = -(hgt[y * w + xb] - hgt[y * w + xa]) * force;
      const ny = (hgt[y1 * w + x] - hgt[y0 * w + x]) * force; // canvas rows run toward -v
      const l = Math.hypot(nx, ny, 1);
      const k = 4 * (y * w + x);
      o[k] = Math.round(127.5 + (127.5 * nx) / l);
      o[k + 1] = Math.round(127.5 + (127.5 * ny) / l);
      o[k + 2] = Math.round(127.5 + 127.5 / l);
      o[k + 3] = 255;
    }
  }
  hgt = null;
  return out;
}

/** Rivet: a small anti-aliased dome on the height canvas. */
function rivet(ctx, x, y, r) {
  const g = ctx.createRadialGradient(x, y, 0, x, y, r);
  g.addColorStop(0, 'rgb(190,190,190)');
  g.addColorStop(0.7, 'rgb(150,150,150)');
  g.addColorStop(1, 'rgb(128,128,128)');
  ctx.fillStyle = g;
  ctx.beginPath(); ctx.arc(x, y, r, 0, 2 * Math.PI); ctx.fill();
}

/* ------------------------------------------------------------------ fuselage atlas */

/** Texture coordinates of a skin point (z, th): u along the length, v around (0 at the belly). */
export const uvFuselage = (z, th) => [(z - FUS.z0) / (FUS.z1 - FUS.z0), (th + Math.PI / 2) / (2 * Math.PI)];

/**
 * Fuselage atlas: albedo (white paint, blue stripe, seam shading, windows cut out in alpha)
 * and normal map (panel grooves, rivet rows, cowl fasteners).
 * @returns {{albedo:any, normale:any}}
 */
export function texturesFuselage(scene, W, H) {
  const px = (z, th) => { const [u, v] = uvFuselage(z, th); return [u * W, (1 - v) * H]; };
  const pxM = W / (FUS.z1 - FUS.z0); // pixels per metre along the length
  const trace = (ctx, pts, fermer = true) => {
    ctx.beginPath();
    pts.forEach(([z, th], i) => { const [x, y] = px(z, th); if (i) ctx.lineTo(x, y); else ctx.moveTo(x, y); });
    if (fermer) ctx.closePath();
  };
  const anneau = (z) => [[z, -Math.PI / 2], [z, 1.5 * Math.PI]];
  const bande = (cote, y0f, y1f, za, zb) => {
    const pts = [];
    for (let z = za; z <= zb + 1e-6; z += 0.02) pts.push([z, angleY(z, y1f(z), cote)]);
    for (let z = zb; z >= za - 1e-6; z -= 0.02) pts.push([z, angleY(z, y0f(z), cote)]);
    return pts;
  };
  const ouv = ouvertures();
  // cheat line rising toward the tail, and a thin pinstripe under it
  const yS = (z) => (z < 0.6 ? -0.2 : -0.2 + (0.5 * (z - 0.6)) / 4.0);
  const lS = (z) => 0.1 + (-0.04 * (z + 2.85)) / 7.45;
  const sillons = [-1.98, -1.75, 1.72, 3.05]; // circumferential skin joints
  const cadres = [-1.07, -0.2, 0.6, 1.2, 2.3, 2.9, 3.6, 4.2]; // frames: rivet rings

  const albedo = texture(scene, 'avion-peau-albedo', W, H, (ctx) => {
    ctx.fillStyle = 'rgb(236,238,240)';
    ctx.fillRect(0, 0, W, H);
    for (const s of [1, -1]) {
      ctx.fillStyle = COULEUR.bleu;
      trace(ctx, bande(s, yS, (z) => yS(z) + lS(z), -2.85, 4.6)); ctx.fill();
      trace(ctx, bande(s, (z) => yS(z) - 0.06, (z) => yS(z) - 0.035, -2.8, 4.5)); ctx.fill();
    }
    // seams catch a little dirt and shade
    ctx.strokeStyle = 'rgba(40,44,52,0.35)';
    ctx.lineWidth = Math.max(1, 0.003 * pxM);
    for (const o of ouv) if (o.kind === 'porte') { trace(ctx, o.pts); ctx.stroke(); }
    for (const z of sillons) { trace(ctx, anneau(z), false); ctx.stroke(); }
    // windows: alpha 0 → cut out by the alpha test
    ctx.globalCompositeOperation = 'destination-out';
    ctx.fillStyle = '#000';
    for (const o of ouv) if (o.kind === 'vitre') { trace(ctx, o.pts); ctx.fill(); }
    ctx.globalCompositeOperation = 'source-over';
  });
  albedo.hasAlpha = true;

  const hc = toile(W, H).getContext('2d', { willReadFrequently: true });
  hc.fillStyle = 'rgb(128,128,128)';
  hc.fillRect(0, 0, W, H);
  hc.strokeStyle = 'rgb(40,40,40)';
  hc.lineWidth = Math.max(1.5, 0.0045 * pxM);
  hc.lineJoin = 'round';
  for (const o of ouv) if (o.kind === 'porte') { trace(hc, o.pts); hc.stroke(); }
  for (const z of sillons) { trace(hc, anneau(z), false); hc.stroke(); }
  // cowling: split line along each side and an oil access door on top
  for (const s of [1, -1]) { trace(hc, [[-2.9, angleY(-2.9, -0.02, s)], [-1.98, angleY(-1.98, 0.02, s)]], false); hc.stroke(); }
  trace(hc, [[-2.2, 1.35], [-2.02, 1.35], [-2.02, 1.79], [-2.2, 1.79]]); hc.stroke();
  // rivet rings on the frames, rivet rows along the tail-cone stringers
  const rr = Math.max(1.2, 0.0028 * pxM);
  const pasTh = (2 * Math.PI) / Math.round((2 * Math.PI * 0.6) / 0.035);
  for (const z of cadres) for (let th = -Math.PI / 2; th < 1.5 * Math.PI; th += pasTh) { const [x, y] = px(z, th); rivet(hc, x, y, rr); }
  for (let k = 0; k < 10; k++) {
    const th = -Math.PI / 2 + (2 * Math.PI * (k + 0.5)) / 10;
    for (let z = 1.75; z < 4.7; z += 0.04) { const [x, y] = px(z, th); rivet(hc, x, y, rr); }
  }
  // cowl fasteners: shallow dimples along the cowl seam
  hc.fillStyle = 'rgb(95,95,95)';
  for (let th = -Math.PI / 2; th < 1.5 * Math.PI; th += pasTh * 4) {
    const [x, y] = px(-2.02, th);
    hc.beginPath(); hc.arc(x, y, rr * 1.6, 0, 2 * Math.PI); hc.fill();
  }
  const img = normales(hc, W, H, 3.0, true);
  const normale = texture(scene, 'avion-peau-normale', W, H, (ctx) => ctx.putImageData(img, 0, 0));
  return { albedo, normale };
}

/* ------------------------------------------------------------------ wing normal map */

/** Wing texture coordinates: u along the span, v around the profile (0.5 at the leading edge). */
export const uvAile = (x, v) => [Math.abs(x) / AILE.bout, v];

/** Wing normal map: skin joints, rib and spar rivet rows, both surfaces. */
export function textureAile(scene, W, H) {
  const px = (x, c, haut) => [(x / AILE.bout) * W, (1 - (haut ? 0.5 - 0.5 * c : 0.5 + 0.5 * c)) * H];
  const hc = toile(W, H).getContext('2d', { willReadFrequently: true });
  hc.fillStyle = 'rgb(128,128,128)';
  hc.fillRect(0, 0, W, H);
  hc.strokeStyle = 'rgb(45,45,45)';
  hc.lineWidth = Math.max(1.5, (0.004 / AILE.bout) * W);
  const segment = (a, b) => { hc.beginPath(); hc.moveTo(...a); hc.lineTo(...b); hc.stroke(); };
  const rr = Math.max(1.2, (0.0026 / AILE.bout) * W);
  for (const haut of [true, false]) {
    for (const x of [1.6, 2.6, 3.6, 4.6]) segment(px(x, 0.12, haut), px(x, 0.72, haut)); // skin joints
    segment(px(0.6, 0.3, haut), px(5.3, 0.3, haut)); // lap joint behind the leading-edge skin
    for (let x = 0.75; x < 5.25; x += 0.33) for (let c = 0.14; c < 0.72; c += 0.025) rivet(hc, ...px(x, c, haut), rr); // ribs
    for (const c of [0.13, 0.25, 0.7]) for (let x = 0.62; x < 5.25; x += 0.035) rivet(hc, ...px(x, c, haut), rr); // spars
  }
  const img = normales(hc, W, H, 2.6, false);
  return texture(scene, 'avion-aile-normale', W, H, (ctx) => ctx.putImageData(img, 0, 0));
}

/* ------------------------------------------------------------------ propeller blur disc */

const DISQUE_VS = `precision highp float;
attribute vec3 position;
uniform mat4 worldViewProjection;
varying vec2 vP;
void main() { vP = position.xy; gl_Position = worldViewProjection * vec4(position, 1.0); }`;

// Exposure-integrated coverage of two blades: the fraction of the shutter time during which a blade
// covers this point. The blades sweep uS radians while the shutter is open, starting at angle uA0.
const DISQUE_FS = `#extension GL_OES_standard_derivatives : enable
precision highp float;
varying vec2 vP;
uniform float uA0;
uniform float uS;
uniform float uR;
uniform float uLum;
uniform vec3 uNoir;
uniform vec3 uBout;
const float PI = 3.14159265;
float corde(float r) {
  float u = r / uR;
  float c = 0.075 + 0.075 * sin(PI * clamp(u * 1.05, 0.0, 1.0));
  if (u > 0.88) c *= sqrt(max(0.0, 1.0 - pow((u - 0.88) / 0.12, 2.0)));
  return c;
}
void main() {
  float r = length(vP);
  float phi = atan(vP.y, vP.x);
  float hw = 0.5 * corde(r) / max(r, 0.05);
  float S = max(uS, min(fwidth(phi), 0.2));
  float cov = 0.0;
  for (int k = 0; k < 2; k++) {
    float d = mod(phi - uA0 - float(k) * PI, 2.0 * PI);
    for (int n = -1; n <= 3; n++) {
      float c0 = d - hw + 2.0 * PI * float(n);
      float c1 = d + hw + 2.0 * PI * float(n);
      cov += max(0.0, min(S, c1) - max(0.0, c0));
    }
  }
  cov = clamp(cov / S, 0.0, 1.0);
  float fr = max(fwidth(r), 1e-4);
  // the eye sees a spinning propeller as a faint disc: alpha 0.12 at the hub to 0.2 near the tips,
  // with the painted tips as a lighter ring; the exposure-integrated blades sit on top of it
  float bord = 1.0 - smoothstep(uR - 1.5 * fr, uR, r);
  float disque = (0.12 + 0.08 * smoothstep(0.25 * uR, 0.9 * uR, r)) * bord;
  float pointe = smoothstep(0.87 * uR - fr, 0.87 * uR + fr, r);
  cov = max(cov, disque + 0.08 * pointe * bord);
  cov *= smoothstep(0.11 - fr, 0.11 + fr, r);
  vec3 col = mix(uNoir, uBout, pointe);
  gl_FragColor = vec4(col * uLum, cov);
}`;

/**
 * Propeller blur disc material (local XY plane, radius R metres).
 * @returns {{mat:any, regler:(a0:number, balayage:number, lum?:number)=>void}}
 */
export function materiauDisque(scene, R) {
  const mat = new B.ShaderMaterial('avion-disque-mat', scene, { vertexSource: DISQUE_VS, fragmentSource: DISQUE_FS }, {
    attributes: ['position'],
    uniforms: ['worldViewProjection', 'uA0', 'uS', 'uR', 'uLum', 'uNoir', 'uBout'],
    needAlphaBlending: true,
  });
  mat.backFaceCulling = false;
  mat.disableDepthWrite = true;
  mat.alphaMode = B.Constants.ALPHA_COMBINE;
  mat.setFloat('uR', R);
  mat.setColor3('uNoir', new B.Color3(0.03, 0.03, 0.035));
  mat.setColor3('uBout', new B.Color3(0.78, 0.8, 0.82));
  let lumiere = 1;
  const regler = (a0, balayage, lum) => {
    if (typeof lum === 'number') lumiere = lum;
    mat.setFloat('uA0', a0);
    mat.setFloat('uS', Math.max(1e-3, balayage));
    mat.setFloat('uLum', lumiere);
  };
  regler(0, 1, 1);
  return { mat, regler };
}
