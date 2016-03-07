var gulp = require('gulp');
var ts = require('gulp-typescript');
var browserSync = require('browser-sync').create();
var sourcemaps = require('gulp-sourcemaps');

var tsProject = ts.createProject('tsconfig.json');
 
gulp.task('compile_ts', function() {
	var tsResult = 
		 tsProject.src()
		.pipe(sourcemaps.init())
		.pipe(ts(tsProject));

	return tsResult.js
		.pipe(sourcemaps.write())
		.pipe(gulp.dest('dist'));
});

gulp.task('compile_ts_then_reload', ['compile_ts'], function() {
    browserSync.reload();
});

gulp.task('serve', ['compile_ts'], function() {
    // Serve files from the root of this project
    browserSync.init({
		proxy: "127.0.0.1:8000"
    });	
    gulp.watch('src/**/*.ts', ['compile_ts_then_reload']);
});



