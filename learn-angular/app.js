var myApp = angular.module('myApp', []);

myApp.controller('mainController', ['$scope', '$filter', '$http', function($scope, $filter, $http) {

    $scope.handle = '';

    $scope.lowercaseHandle = function () {
        return $filter('lowercase')($scope.handle);
    }

}]);
