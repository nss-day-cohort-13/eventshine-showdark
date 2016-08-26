var app = angular
    .module("TicketApp", [])
    .config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('((');
        $interpolateProvider.endSymbol('))');},
        
        ['$httpProvider', function($httpProvider) {
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }]);
