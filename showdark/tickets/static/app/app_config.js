app
    // Takes out the # in the url
    // .config(function($locationProvider) {
    //     $locationProvider.html5Mode(true);
    // });
    .config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/myEvents', {
                templateUrl: 'static/app/partials/user_events.html',
                controller: 'UserEventsCtrl',
                // controllerAs: 'userEvents'
            })
            .when('/allEvents', {
                templateUrl: 'static/app/partials/all_events.html',
                controller: 'AllEventsCtrl',
                // controllerAs: 'allEvents'
            })
        // Still needs the rest of the routes
    }])
