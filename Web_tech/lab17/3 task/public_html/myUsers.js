var app = angular.module('myApp', ['ngRoute']);
app.config(function($routeProvider){
    $routeProvider
    .when("/", {templateUrl : "./routes/about_me.html"})
    .when("/projects", {templateUrl : "./routes/projects.html"})
    .when("/image", {templateUrl : "./routes/image.html"})
    .when("/contact_me", {templateUrl : "./routes/contact_me.html"})
    .otherwise({
        redirectTo: "/"
    });
})


