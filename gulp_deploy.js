//this file is run on travis ci server
var gulp = require('gulp');
var ts = require('gulp-typescript');
var uglify = require('gulp-uglify');
var shell = require('gulp-shell');
var run_sequence = require('run-sequence');

var tsProject = ts.createProject('./static/tsconfig.json',{outFile:'ndc_bundle.js'});
gulp.task('compile_ts',function(){
	var tsResult = 
		 tsProject.src()
		.pipe(ts(tsProject));

	return tsResult.js
		.pipe(uglify())	
		.pipe(gulp.dest('./static/build'));	
});

gulp.task('collect_static', shell.task([
  // 'honcho run python manage.py collectstatic --noinput -i .bin -i angular2 -i es6-promise -i es6-shim -i reflect-metadata -i rxjs -i systemjs -i typings -i zone.js'
  'ls'
]));

gulp.task('default',function(cb){
	run_sequence(
		'compile_ts',
		'collect_static',
		cb
	);
});
