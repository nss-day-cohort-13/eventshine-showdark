angular.module('app').config(function($routeProvider) {   // Takes out the # in the url
    // .config(function($locationProvider) {
    //     $locationProvider.html5Mode(true);
    // });

        $routeProvider
            .when('/', {
                templateUrl: 'partials/user_events.html',
                controller: 'UserEventsCtrl',
                // controllerAs: 'userEvents'
            })
            .when('/allEvents', {
                templateUrl: 'static/app/partials/all_events.html',
                controller: 'AllEventsCtrl',
                // controllerAs: 'allEvents'
            })
        // Still needs the rest of the routes
    })
