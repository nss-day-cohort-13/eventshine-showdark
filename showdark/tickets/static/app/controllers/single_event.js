"use strict";

angular.module('app').controller("SingleEventCtrl", function ($scope, $http, $routeParams) {
	$scope.title = "Event";
	$scope.current_user = $http.get("http://localhost:8000/tickets/")
		.then((res) => {
        	$scope.user = res;
        });

	// $http.get("localhost:8000/tickets/event/")
	//     .then((res) => $scope.venues = res.data)

	$scope.events = [];
});
