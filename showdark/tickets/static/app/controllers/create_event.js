app.controller("CreateEventCtrl", function ($scope, $http) {

    $scope.title = "Create an event!"
    $scope.venues = []

    // get all venues for form dropdown
    $http.get("localhost:8000/tickets/venues")
        .then((res) => $scope.venues = res.data)
})
