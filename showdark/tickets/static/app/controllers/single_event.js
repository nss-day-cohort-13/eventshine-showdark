"use strict";

	// NOT YET IMPLEMENTED !!!!
angular.module('app').controller("SingleEventCtrl", function ($scope, $http, $routeParams) {
	$scope.title = "Events";
	$scope.current_user = // figure out how to get the current user

	// $http.get("localhost:8000/tickets/event/")
	//     .then((res) => $scope.venues = res.data)

	$scope.events = [];
});
