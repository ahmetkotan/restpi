var app = angular.module('pinTableApp', []);
    app.controller('pinTableController', function($scope, $http) {
        $http.get("/pins/api/")
            .then(function(response) {
                var pins = response.data.results;
                var new_pinlist = [];
                var temp_pinlist = [];
                pins.forEach(function (item, index) {
                    if(index % 2 == 0){
                        temp_pinlist.push(item);
                    }else{
                        temp_pinlist.push(item);
                        new_pinlist.push(temp_pinlist);
                        temp_pinlist = []
                    }
                });
                $scope.pins = new_pinlist;
            });
    });