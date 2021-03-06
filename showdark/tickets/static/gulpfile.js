"use-strict"

const gulp = require("gulp")
const sass = require("gulp-sass")

gulp.task("sass", function() {
	return gulp.src("sass/main.sass")
	.pipe(sass())
	.pipe(gulp.dest("css"))
})

gulp.task("watch", function () {
	gulp.watch("sass/main.sass", ["sass"])
})

gulp.task("default", ["sass", "watch"])
