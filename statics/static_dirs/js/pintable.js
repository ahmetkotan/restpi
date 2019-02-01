var app = angular.module('pinTableApp', []);
app.controller('pinTableController', function($scope, $http) {
    $scope.refresh_list = function(){
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

    var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    $http.get("/pins/api/")
        .then(function(response) {
            $scope.pinlist = response.data.results;
            $scope.pins = $scope.refresh_list();
        });

    $scope.change_mode = function (physical, mode_code) {
        var url = "/pins/api/" + physical;
        $http.post(url,
            {mode: mode_code},
            {headers: {'Content-Type': 'application/json', 'X-CSRFToken': token}})
            .then(function (response) {
                if(response.data.operation){
                    $scope.pinlist[physical-1] = response.data.pin;
                    $scope.pins = $scope.refresh_list();
                }
            })
            .catch((err) => {
                var error_msg, footer_msg = '';
                console.log(err);
                if(err.status == 403){
                    error_msg = err.data.detail;
                    footer_msg = '<a href="/login">Login</a>';
                }else{
                    error_msg = err.data.mode
                }
                Swal.fire({
                    type: 'error',
                    title: 'Oops...',
                    text: error_msg,
                    footer: footer_msg
                });
                $scope.pins = $scope.refresh_list();
            })
    };

    $scope.change_value = function (physical) {
        var url = "/pins/api/" + physical;
        var new_value = ($scope.pinlist[physical-1].value) ? 0 : 1
        $http.post(url,
            {value: new_value},
            {headers: {'Content-Type': 'application/json', 'X-CSRFToken': token}})
            .then(function (response) {
                if(response.data.operation){
                    $scope.pinlist[physical-1] = response.data.pin;
                    $scope.pins = $scope.refresh_list();
                }
            })
            .catch((err) => {
                var error_msg, footer_msg = '';
                if(err.status == 403){
                    error_msg = err.data.detail;
                    footer_msg = '<a href="/login">Login</a>';
                }else{
                    error_msg = err.data.value
                }
                Swal.fire({
                    type: 'error',
                    title: 'Oops...',
                    text: error_msg,
                    footer: footer_msg
                });
                $scope.pins = $scope.refresh_list();
            })
    }

});