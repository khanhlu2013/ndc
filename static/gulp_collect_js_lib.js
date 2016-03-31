var gulp = require('gulp');
var shell = require('gulp-shell');

gulp.task('default',shell.task([
	'rm -rf collected_js_lib', 
	'mkdir collected_js_lib',
	'cp ./node_modules/es6-shim/es6-shim.min.js ./collected_js_lib',
	'cp ./node_modules/systemjs/dist/system-polyfills.js ./collected_js_lib',
	'cp ./node_modules/angular2/bundles/angular2-polyfills.js ./collected_js_lib',
	'cp ./node_modules/systemjs/dist/system.src.js ./collected_js_lib',
	'cp ./node_modules/rxjs/bundles/Rx.js ./collected_js_lib',
	'cp ./node_modules/angular2/bundles/angular2.dev.js ./collected_js_lib',
	'cp ./node_modules/angular2/bundles/router.dev.js ./collected_js_lib',
	'cp ./node_modules/angular2/bundles/http.dev.js ./collected_js_lib'
]));