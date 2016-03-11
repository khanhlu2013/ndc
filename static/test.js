var Builder = require('systemjs-builder');

// optional constructor options
// sets the baseURL and loads the configuration file
var builder = new Builder('.');

builder.buildStatic('dist/ndc_resource.js', 'dist/ndc_resource_sfx.js', { runtime: true });