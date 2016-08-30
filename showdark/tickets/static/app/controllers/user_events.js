angular.module('app').controller("UserEventsCtrl", function ($scope, $http){

    $scope.title = "My Events"
    let current_user_id = // figure out how to get the current user

    $scope.user_events = []
    $scope.event_venues = []

    // Gets all events with the user id of the current user
    $http.get(`http://localhost:8000/tickets/${current_user_id}`)
        .then((res) => $scope.user_events = res.data)

    // Gets all venues
    $http.get('http://localhost:8000/tickets/venues')
        .then((res) => $scope.event_venues = res.data)

    // $scope.delete_event = () => {
    //     $http.delete(`http://localhost:8000/tickets/${current_user_id}`)
    // }
})
