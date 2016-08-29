app.config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/myEvents', {
                templateUrl: 'partials/user_events.html',
                controller: 'UserEventsCtrl',
                // controllerAs: 'userEvents'
            })
            .when('/allEvents', {
                templateUrl: 'partials/all_events.html',
                controller: 'AllEventsCtrl',
                // controllerAs: 'allEvents'
            })
    }])
