/**
 * Created by smuravko on 29.07.15.
 */

/**
 * Created by smuravko on 20.12.14.
 */
// ['angular-loading-bar', 'ngAnimate']

var app = angular.module("demoapp", ['ngRoute', 'angularFileUpload']);

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

