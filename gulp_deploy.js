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
  'python manage.py collectstatic --noinput'
  //make sure we set DISABLE_COLLECTSTATIC = true @ heroku. if we don't, it is not a fatal problem. heroku will smart enough to detect unmodification.
]));

gulp.task('clean_up',shell.task([
	'rm -rf ./node_modules',
	'rm -rf ./static/node_modules',
	'rm -rf ./static/typings'
]));

gulp.task('default',function(cb){
	run_sequence(
		'compile_ts',
		'collect_static',
		'clean_up',
		cb
	);
});
