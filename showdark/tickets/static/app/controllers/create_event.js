angular.module('app').controller("CreateEventCtrl", function ($scope, $http) {

    $scope.title = "Create an event!"
    $scope.venues = []

    // get all venues for form dropdown
    $http.get("localhost:8000/tickets/venues")
        .then((res) => $scope.venues = res.data)

    $scope.create_event = function () {
    	$http.post("localhost:8000/tickets/profile/create_event", {
    		eventName: $scope.eventName,
    		description: $scope.description,
    		city: $scope.city,
    		beginTime: $scope.beginTime,
    		endTime: $scope.endTime,
    		venue: $scope.venue
    	})
    	.then((res) => {
    		console.log("POSTED!");
    	})
    }
})
