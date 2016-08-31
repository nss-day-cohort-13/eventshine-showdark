angular.module('app').controller("CreateEventCtrl", function ($scope, $http, $location) {

    $scope.title = "Create an event!"
    $scope.venues = []

    // get all venues for form dropdown
    $http.get("http://localhost:8000/tickets/venues")
        .then((res) => $scope.venues = res.data)


    $scope.create_event = function () {
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

    $scope.backToProfile = () => {
      $location.path('/');
    }

    $scope.allEvents = () => {
      $location.path('/allEvents');

})
