app.controller("UserEventsCtrl", function ($scope, $http){

    $scope.title = "My Events"
    let current_user_id = // figure out how to get the current user

    $scope.user_events = []

    $http.get(`http://localhost:8000/tickets/${current_user_id}`)
     .then((res) => $scope.user_events = res.data)

    // $scope.delete_event = () => {
    //     $http.delete(`http://localhost:8000/tickets/${current_user_id}`)
    // }
})
