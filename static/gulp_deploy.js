//this file is run on travis ci server
var gulp = require('gulp');
var ts = require('gulp-typescript');
var uglify = require('gulp-uglify');


var tsProject = ts.createProject('tsconfig.json',{outFile:'ndc_bundle.js'});
gulp.task('default',function(){
	var tsResult = 
		 tsProject.src()
		.pipe(ts(tsProject));

	return tsResult.js
		.pipe(uglify())	
		.pipe(gulp.dest('build/deploy'));	
});