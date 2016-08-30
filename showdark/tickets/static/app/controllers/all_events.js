angular.module('app').controller("AllEventsCtrl", function ($scope, $http){

    $scope.title = "Events"
    $scope.current_user = // figure out how to get the current user

    $scope.events = []

    // Request for every event
    $http.get("http://localhost:8000/tickets/events")
     .then((res) => $scope.events = res.data)

    // Is not connnected yet. This is supposed to register the user when
    // they click the register button on one of the events on the all events page.
    $scope.register_for_event = (event) => {
        $http.post("http://localhost:8000/tickets/event_registration", {userId: $scope.current_user, eventID: event.pk})
        .then((res) => {
            // "registration successful" message
        },
        (rej) => {
            // "failed to register" message
        })
    }

})
