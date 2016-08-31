angular.module('app').controller("CreateEventCtrl", function ($scope, $http, $location, $timeout) {

    $scope.title = "Create an event!"
    $scope.venues = []

    // get all venues for form dropdown
    $http.get("http://localhost:8000/tickets/venues")
        .then((res) => $scope.venues = res.data)

    $scope.create_event = function () {
    	console.log("EVENT-VENUE: ", $scope.venue);
    	$http({
    		url: "http://localhost:8000/tickets/create_event",
	    	method: "POST",
	    	data: {
	    		eventName: $scope.eventName,
	    		description: $scope.description,
	    		city: $scope.city,
	    		beginTime: $scope.beginTime,
	    		endTime: $scope.endTime,
	    		venue: $scope.venue
	    	}
    	})
    	.then((res) => {
    		$location.path("/allEvents")
    	})
    }
})
