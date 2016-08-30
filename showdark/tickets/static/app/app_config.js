angular.module('app').config(function($routeProvider) {   // Takes out the # in the url
    // .config(function($locationProvider) {
    //     $locationProvider.html5Mode(true);
    // });

        $routeProvider
            .when('/', {
                templateUrl: '/static/app/partials/user_events.html',
                controller: 'UserEventsCtrl',
                // controllerAs: 'userEvents'
            })
            .when('/allEvents', {
                templateUrl: '/static/app/partials/all_events.html',
                controller: 'AllEventsCtrl',
                // controllerAs: 'allEvents'
            })
            .when('/createEvent', {
                templateUrl: '/static/app/partials/create_event.html',
                controller: 'CreateEventCtrl',
                // controllerAs: 'createEvent'
    })
