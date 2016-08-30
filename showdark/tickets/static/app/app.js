var app = angular
    .module("TicketApp", [])
	.value('loggedInUser', '')
    .config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('((');
        $interpolateProvider.endSymbol('))');},
        
        ['$httpProvider', function($httpProvider) { // This was suggested by an article to fix csrf errors
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }]);
