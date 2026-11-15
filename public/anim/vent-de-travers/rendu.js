// Copyright: Your Name. Apache 2.0
// Offline render mode of « Vent de travers ». For one film time t, the engine draws N sub-frames with
// sub-pixel camera jitter (Halton 2,3) and sub-frame time offsets inside a 180° shutter at 30 fps.
// Each sub-frame is copied from the engine canvas into a float framebuffer of a small separate WebGL2
// context (linear light, additive blending), then the average is presented on an overlay canvas.
// Result: anti-aliasing, true motion blur. HTML text stays crisp on top (drawn once, not accumulated).

import { DUREE, PLANS, planA } from './communs.js';

/** Radical inverse in base b: the Halton sequence (index starts at 1). */
export function halton(i, b) {
  let f = 1;
  let r = 0;
  let n = i;
  while (n > 0) {
    f /= b;
    r += f * (n % b);
    n = Math.floor(n / b);
  }
  return r;
}

/** Shutter: 180° at 30 fps, i.e. the frame is exposed during 1/60 s centred on t. */
export const OBTURATION = 0.5 / 30;

/**
 * Time of sub-frame i (of n) for frame time t, kept inside the scene of t: a sub-frame never shows
 * the other scene across a cut (no cross-scene blending).
 */
export function tempsSousImage(t, i, n) {
  const brut = n <= 1 ? t : t + ((i + 0.5) / n - 0.5) * OBTURATION;
  let ts = Math.min(DUREE - 1e-4, Math.max(0, brut));
  const scene = PLANS[planA(t)].scene;
  if (PLANS[planA(ts)].scene !== scene) {
    // clamp to the boundary of the shot that contains t
    const [a, b] = PLANS[planA(t)].t;
    ts = Math.min(b - 1e-4, Math.max(a, ts));
  }
  return ts;
}

/**
 * Projection-matrix copy shifted by (dx, dy) render pixels. Works for perspective and orthographic
 * matrices: clip.xy += offsetNdc * clip.w.
 * @param {any} proj BABYLON.Matrix
 * @param {number} dx pixels
 * @param {number} dy pixels
 * @param {number} w render width in pixels
 * @param {number} h render height in pixels
 */
export function projectionDecalee(proj, dx, dy, w, h) {
  const m = proj.clone();
  const a = m.m.slice ? Array.from(m.m) : [...m.m];
  const ox = (2 * dx) / w;
  const oy = (2 * dy) / h;
  for (const [c, ligne] of [[0, ox], [1, oy]]) {
    // column-major storage: element (row r, column k) is a[k * 4 + r]
    for (let k = 0; k < 4; k += 1) a[k * 4 + c] += ligne * a[k * 4 + 3];
  }
  return BABYLON.Matrix.FromArray(a);
}

const VS = `#version 300 es
in vec2 p; out vec2 uv;
void main() { uv = p * 0.5 + 0.5; gl_Position = vec4(p, 0.0, 1.0); }`;

// sRGB 8-bit sample -> linear, pre-weighted by 1/N
const FS_ACCUM = `#version 300 es
precision highp float;
in vec2 uv; uniform sampler2D img; uniform float poids; out vec4 o;
vec3 lin(vec3 c) { return mix(c / 12.92, pow((c + 0.055) / 1.055, vec3(2.4)), step(0.04045, c)); }
void main() { o = vec4(lin(texture(img, uv).rgb) * poids, poids); }`;

// linear average -> sRGB, opaque
const FS_PRESENT = `#version 300 es
precision highp float;
in vec2 uv; uniform sampler2D acc; out vec4 o;
vec3 srgb(vec3 c) { c = clamp(c, 0.0, 1.0); return mix(c * 12.92, 1.055 * pow(c, vec3(1.0 / 2.4)) - 0.055, step(0.0031308, c)); }
void main() { vec4 a = texture(acc, uv); o = vec4(srgb(a.rgb / max(a.a, 1e-6)), 1.0); }`;

function programme(gl, fs) {
  const compiler = (type, src) => {
    const s = gl.createShader(type);
    gl.shaderSource(s, src);
    gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(`accumulateur : ${gl.getShaderInfoLog(s)}`);
    return s;
  };
  const p = gl.createProgram();
  gl.attachShader(p, compiler(gl.VERTEX_SHADER, VS));
  gl.attachShader(p, compiler(gl.FRAGMENT_SHADER, fs));
  gl.bindAttribLocation(p, 0, 'p');
  gl.linkProgram(p);
  if (!gl.getProgramParameter(p, gl.LINK_STATUS)) throw new Error(`accumulateur : ${gl.getProgramInfoLog(p)}`);
  return p;
}

/**
 * Float accumulation buffer on its own WebGL2 canvas (placed over the engine canvas).
 * @param {HTMLCanvasElement} toile overlay canvas
 */
export function creerAccumulateur(toile) {
  const gl = toile.getContext('webgl2', { alpha: false, antialias: false, preserveDrawingBuffer: true, premultipliedAlpha: false });
  if (!gl) throw new Error('WebGL2 indisponible pour l’accumulation');
  if (!gl.getExtension('EXT_color_buffer_float')) throw new Error('EXT_color_buffer_float indisponible');
  const float32 = !!gl.getExtension('EXT_float_blend');
  const formatInterne = float32 ? gl.RGBA32F : gl.RGBA16F;
  const typeTexel = float32 ? gl.FLOAT : gl.HALF_FLOAT;

  const pAccum = programme(gl, FS_ACCUM);
  const pPresent = programme(gl, FS_PRESENT);
  const vbo = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, vbo);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
  gl.enableVertexAttribArray(0);
  gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);

  const texSource = gl.createTexture();
  const texAcc = gl.createTexture();
  const fbo = gl.createFramebuffer();
  let w = 0;
  let h = 0;
  const regler = (tex) => {
    gl.bindTexture(gl.TEXTURE_2D, tex);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
  };
  regler(texSource);
  regler(texAcc);

  function dimensionner(largeur, hauteur) {
    if (largeur === w && hauteur === h) return;
    w = largeur;
    h = hauteur;
    toile.width = w;
    toile.height = h;
    gl.bindTexture(gl.TEXTURE_2D, texAcc);
    gl.texImage2D(gl.TEXTURE_2D, 0, formatInterne, w, h, 0, gl.RGBA, typeTexel, null);
    gl.bindFramebuffer(gl.FRAMEBUFFER, fbo);
    gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, texAcc, 0);
    if (gl.checkFramebufferStatus(gl.FRAMEBUFFER) !== gl.FRAMEBUFFER_COMPLETE) throw new Error('tampon flottant incomplet');
    gl.bindFramebuffer(gl.FRAMEBUFFER, null);
  }

  return {
    float32,
    dimensionner,
    vider() {
      gl.bindFramebuffer(gl.FRAMEBUFFER, fbo);
      gl.viewport(0, 0, w, h);
      gl.clearColor(0, 0, 0, 0);
      gl.clear(gl.COLOR_BUFFER_BIT);
    },
    /** Adds the current content of `source` (a canvas of the same size) with weight `poids`. */
    ajouter(source, poids) {
      gl.bindTexture(gl.TEXTURE_2D, texSource);
      gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, true);
      gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, false);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA8, gl.RGBA, gl.UNSIGNED_BYTE, source);
      gl.bindFramebuffer(gl.FRAMEBUFFER, fbo);
      gl.viewport(0, 0, w, h);
      gl.enable(gl.BLEND);
      gl.blendFunc(gl.ONE, gl.ONE);
      gl.useProgram(pAccum);
      gl.uniform1i(gl.getUniformLocation(pAccum, 'img'), 0);
      gl.uniform1f(gl.getUniformLocation(pAccum, 'poids'), poids);
      gl.activeTexture(gl.TEXTURE0);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
      gl.disable(gl.BLEND);
    },
    presenter() {
      gl.bindFramebuffer(gl.FRAMEBUFFER, null);
      gl.viewport(0, 0, w, h);
      gl.useProgram(pPresent);
      gl.activeTexture(gl.TEXTURE0);
      gl.bindTexture(gl.TEXTURE_2D, texAcc);
      gl.uniform1i(gl.getUniformLocation(pPresent, 'acc'), 0);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
      gl.finish();
    },
  };
}

const image = () => new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)));

/**
 * Offline renderer.
 * @param {{
 *   moteur: any,                       // BABYLON.Engine
 *   toile: HTMLCanvasElement,          // accumulation overlay canvas
 *   dimensionner: (l: number, h: number) => void, // sizes the film frame (CSS px = render px)
 *   dessiner: (t: number, jitter: {dx:number, dy:number}|null) => void, // renders the engine canvas at t
 *   texte: (t: number) => void,        // updates the HTML text for t (once per frame)
 * }} o
 */
export function creerRendu(o) {
  let acc = null;
  return {
    /**
     * Renders film time t with N accumulated sub-frames; resolves when the page shows the final frame.
     * @param {number} t
     * @param {{ largeur?: number, hauteur?: number, echantillons?: number }} [options]
     */
    async rendre(t, options = {}) {
      const largeur = Math.round(options.largeur || o.moteur.getRenderWidth());
      const hauteur = Math.round(options.hauteur || o.moteur.getRenderHeight());
      const n = Math.max(1, Math.min(256, Math.round(options.echantillons || 16)));
      o.dimensionner(largeur, hauteur);
      if (!acc) acc = creerAccumulateur(o.toile);
      const w = o.moteur.getRenderWidth();
      const h = o.moteur.getRenderHeight();
      acc.dimensionner(w, h);
      o.toile.style.display = 'block';
      acc.vider();
      const tf = Math.min(DUREE, Math.max(0, Number(t) || 0));
      for (let i = 0; i < n; i += 1) {
        const jitter = n <= 1 ? null : { dx: halton(i + 1, 2) - 0.5, dy: halton(i + 1, 3) - 0.5 };
        o.dessiner(tempsSousImage(tf, i, n), jitter);
        acc.ajouter(o.moteur.getRenderingCanvas(), 1 / n);
      }
      acc.presenter();
      o.texte(tf);
      await image();
      return { t: tf, largeur: w, hauteur: h, echantillons: n, float32: acc.float32 };
    },
  };
}
