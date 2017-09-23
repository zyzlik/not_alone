app = angular.module('cases', []);

app.controller('CaseListController', ['$scope', '$http', function($scope, $http) {
    $scope.cases = [];
    $http.get('/api-v1/cases').then(function(result) {
        angular.forEach(result.data, function(item) {
            $scope.cases.push(item);
        });
    });
}]);