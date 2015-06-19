// File: Gulpfile.js
'use strict';
var gulp = require('gulp'),
connect = require('gulp-connect'),
 stylus = require('gulp-stylus'),
 nib = require('nib'),
 jshint = require('gulp-jshint'),
 stylish = require('jshint-stylish'),
 historyApiFallback = require('connect-history-api-fallback');
// Servidor web de desarrollo
gulp.task('server', function() {
 connect.server({
 root: './Frontend',
 hostname: '0.0.0.0',
 port: 8080,
 livereload: true,
 middleware: function(connect, opt) {
 return [ historyApiFallback ];
 }
 });
});
// Busca errores en el JS y nos los muestra por pantalla
gulp.task('jshint', function() {
 return gulp.src('./Frontend/js/**/*.js')
 .pipe(jshint('.jshintrc'))
 .pipe(jshint.reporter('jshint-stylish'))
 .pipe(jshint.reporter('fail'));
});
// Preprocesa archivos Stylus a CSS y recarga los cambios
//gulp.task('css', function() {
// gulp.src('./app/stylesheets/main.styl')
// .pipe(stylus({ use: nib() }))
// .pipe(gulp.dest('./app/stylesheets'))
// .pipe(connect.reload());
//});
// Recarga el navegador cuando hay cambios en el HTML
gulp.task('html', function() {
 gulp.src('./Frontend/**/*.html')
 .pipe(connect.reload());
});
// Vigila cambios que se produzcan en el código
// y lanza las tareas relacionadas
gulp.task('watch', function() {
 gulp.watch(['./Frontend/**/*.html'], ['html']); //gulp.watch(['./Frontend/css/**/*.styl'], ['css']);
 gulp.watch(['./Frontend/js/**/*.js', './Gulpfile.js'], ['jshint']);
});
gulp.task('default', ['server', 'watch']);

//var inject = require('gulp-inject');
//var wiredep = require('wiredep').stream;
// Busca en las carpetas de estilos y javascript los archivos que hayamos creado
// para inyectarlos en el index.html
//gulp.task('inject', function() {
// var sources = gulp.src(['./Frontend/scripts/**/*.js','./Frontend/stylesheets/**/*.css']);
// return gulp.src('index.html', {cwd: './app'})
// .pipe(inject(sources, {
// read: false,
// ignorePath: '/app'
// }))
// .pipe(gulp.dest('./app'));
//});
// Inyecta las librerias que instalemos vía Bower
//gulp.task('wiredep', function () {
// gulp.src('./Frontend/index.html')
// .pipe(wiredep({
// directory: './Frontend/lib'
// }))
// .pipe(gulp.dest('./Frontend'));
//});
//gulp.task('watch', function() {
//// //gulp.watch(['./app/stylesheets/**/*.styl'], ['css', 'inject']);
// gulp.watch(['./Frontend/js/**/*.js', './Gulpfile.js'], ['jshint', 'inject']);
//// //gulp.watch(['./bower.json'], ['wiredep']);
//});
//gulp.task('default', ['server', 'inject', 'wiredep', 'watch']);
