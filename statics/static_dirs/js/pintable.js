var app = angular.module('pinTableApp', []);
app.controller('pinTableController', function($scope, $http) {
    $scope.refresh_list = function(pin_list){
        var new_pinlist = [];
        var temp_pinlist = [];
        $scope.pinlist.forEach(function (item, index) {
            if(index % 2 == 0){
                temp_pinlist.push(item);
            }else{
                temp_pinlist.push(item);
                new_pinlist.push(temp_pinlist);
                temp_pinlist = []
            }
        });
        return new_pinlist;
    };

    $http.get("/pins/api/")
        .then(function(response) {
            $scope.pinlist = response.data.results;
            $scope.pins = $scope.refresh_list($scope.pinlist);
        });

    $scope.change_mode = function (physical, mode_code) {
        var url = "/pins/api/" + physical;
        $http.post(url, {mode: mode_code}, {headers: {'Content-Type': 'application/json'}})
            .then(function (response) {
                if(response.status == 200 && response.data.operation){
                    $scope.pinlist[physical-1] = response.data.pin;
                    $scope.pins = $scope.refresh_list($scope.pinlist);
                }
            })
            .catch((err) => {
                $scope.pins = $scope.refresh_list($scope.pinlist);
            })
    }

});

$(document).ready(function() {
    $('.container').on('click', '.radioBtn a', function() {
        var sel = $(this).data('title');
        var tog = $(this).data('toggle');
        $(this).parent().next('.' + tog).prop('value', sel);
        $(this).parent().find('a[data-toggle="' + tog + '"]').not('[data-title="' + sel + '"]').removeClass('active').addClass('notActive');
        $(this).parent().find('a[data-toggle="' + tog + '"][data-title="' + sel + '"]').removeClass('notActive').addClass('active');
    });
});