angular.module('app').controller("CreateEventCtrl", function ($scope, $http, $location) {

    $scope.title = "Create an event!"
    $scope.venues = []

    // get all venues for form dropdown
    $http.get("localhost:8000/tickets/venues")
        .then((res) => $scope.venues = res.data)

    $scope.backToProfile = () => {
      $location.path('/');
    }

    $scope.allEvents = () => {
      $location.path('/allEvents');
    }


})
