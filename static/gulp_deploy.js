//this file is run on travis ci server
var gulp = require('gulp');
var shell = require('gulp-shell')
var ts = require('gulp-typescript');
var uglify = require('gulp-uglify');

gulp.task('install_typings', shell.task([
  'typings install',
]))

var tsProject = ts.createProject('tsconfig.json',{outFile:'ndc_bundle.js'});
gulp.task('default',['install_typings'],function(){
	var tsResult = 
		 tsProject.src()
		.pipe(ts(tsProject));

	return tsResult.js
		.pipe(uglify())	
		.pipe(gulp.dest('build/deploy'));	
});