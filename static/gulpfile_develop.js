var gulp = require('gulp');
var ts = require('gulp-typescript');
var browserSync = require('browser-sync').create();
var sourcemaps = require('gulp-sourcemaps');
var runSequence = require('run-sequence');

var tsProject = ts.createProject('tsconfig.json',{outFile:'ndc_bundle.js'});
gulp.task('build_develop_js',function(){
	var tsResult = 
		 gulp.src(['src/**/*.ts','typings/browser/**/*.d.ts'])
		.pipe(sourcemaps.init())
		.pipe(ts(tsProject));

	return tsResult.js
		.pipe(sourcemaps.write())
		.pipe(gulp.dest('build/develop'));	
});
gulp.task('refresh_browser',function(){
	console.log('im here');
	return browserSync.reload();
})
gulp.task('build_develop_nWatch2RefreshBrowser', ['build_develop_js'], function() {
    browserSync.init({
		proxy: "127.0.0.1:8000"
    });
    gulp.watch('src/**/*.ts', function(){
		runSequence(
			['build_develop_js'],
			['refresh_browser']
		);
    });
    gulp.watch('./../templates/manage_app.html', ['refresh_browser']);
});