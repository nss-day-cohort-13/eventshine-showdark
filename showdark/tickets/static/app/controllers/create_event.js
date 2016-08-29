app.controller("CreateEventCtrl", function ($scope, $http) {

    $scope.title = "Create and event!"
    $scope.venues = []

    $http.get("localhost:8000/tickets/venues")
        .then((res) => $scope.venues = res.data)

    $scope.create_event = (event) => {
        $http.post("localhost:8000/tickets/create_event",
            {
                name: $scope.eventName,
                description: $scope.description,
                city: $scope.city,
                startDate: $scope.start,
                endDate: $scope.end,
                venueId: $scope.venue.pk
            })
            .then((res) => {
                // "successfully created event"
            }),
            (rej) => {
                // "error, try again"
            }
    }
})
