var app = angular
    .module("TicketApp", [])
    .config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('((');
        $interpolateProvider.endSymbol('))');
    });
