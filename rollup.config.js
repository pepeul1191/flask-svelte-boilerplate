import svelte from 'rollup-plugin-svelte';
import commonjs from '@rollup/plugin-commonjs';
import terser from '@rollup/plugin-terser';
import resolve from '@rollup/plugin-node-resolve';
import postcss from 'rollup-plugin-postcss';
import postcssImport from 'postcss-import';
import autoprefixer from 'autoprefixer';
import copy from 'rollup-plugin-copy';
import { defineConfig } from 'rollup';

const production = !process.env.ROLLUP_WATCH;

const Vendor = {
  input: 'src/entries/vendor.js',
  output: {
    sourcemap: true,
    format: 'iife',
    name: 'vendor',
    file: production ? 'static/dist/vendor.min.js' : 'static/dist/vendor.js',
    globals: {
      'bootstrap': 'bootstrap'
    }
  },
  plugins: [
    svelte({
      compilerOptions: {
        dev: !production
      }
    }),

    postcss({
      extract: 'vendor.min.css',
      minimize: production,
      sourceMap: !production,
      plugins: [
        postcssImport(),
        autoprefixer()
      ]
    }),

    resolve({
      browser: true,
      dedupe: ['svelte'],
      exportConditions: ['svelte']
    }),

    commonjs(),

    production && terser(),

    copy({
      hook: 'writeBundle',
      targets: [
        {
          src: 'node_modules/font-awesome/fonts/*',
          dest: 'static/fonts/'
        },
        {
          src: 'node_modules/simplemde/dist/*',
          dest: 'static/dist/'
        }
      ]
    })
  ],
  watch: {
    clearScreen: false
  }
};

const App = {
  input: 'src/entries/app.js',
  output: {
    file: 'static/dist/app.min.js',
    format: 'iife',
    sourcemap: !production
  },
  plugins: [
    svelte({
      compilerOptions: {
        dev: !production
      }
    }),

    postcss({
      extract: 'app.min.css',
      minimize: production,
      sourceMap: !production,
      plugins: [
        postcssImport(),
        autoprefixer()
      ]
    }),

    resolve({
      browser: true,
      dedupe: ['svelte']
    }),

    commonjs(),

    production && terser(),

    copy({
      targets: [
        { src: 'src/assets/*', dest: 'static/dist/assets' }
      ]
    })
  ],
  watch: {
    clearScreen: false
  }
};

export default defineConfig([App, Vendor]);
