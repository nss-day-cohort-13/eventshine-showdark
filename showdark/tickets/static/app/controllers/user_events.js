angular.module('app').controller("UserEventsCtrl", function ($scope, $http, $timeout, $location){


    $scope.title = "My Events"
    $http.get(`http://localhost:8000/tickets/get_user/`)
      .then(function success (res){
        return $scope.current_user = res.data[0];
      }) // figure out how to get the current user

    $timeout(function events() {
      $http.get(`http://localhost:8000/tickets/${$scope.current_user.pk}`)
          .then((res) => $scope.user_events = res.data)
    }, 2000)
    // Gets all events with the user id of the current user
    // $http.get(`http://localhost:8000/tickets/${$scope.current_user.pk}`)
    //     .then((res) => $scope.user_events = res.data);

    // Gets all venues
    $http.get('http://localhost:8000/tickets/venues')
        .then((res) => $scope.event_venues = res.data);

    $scope.create_event = function () {
        $location.path("/createEvent")
    }

    // $scope.delete_event = () => {
    //     $http.delete(`http://localhost:8000/tickets/${current_user_id}`)
    // }

    $scope.allEvents = () => {
      $location.path('/allEvents');
    }
})
