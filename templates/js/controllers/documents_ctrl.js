/**
 * Created by smuravko on 25.01.15.
 */

app.controller('DocumentCtrl', ['$rootScope', '$scope', '$http',
    '$anchorScroll', '$location', '$document',
    function($rootScope, $scope, $http, $anchorScroll, $location, $document
        ) {

        $scope.permitUser = '';
        $scope.get_documents = function() {
            $http.get('../api/documents/')
                .success(function (data) {
                    $scope.documents = data;
                });
        };
        $scope.get_documents();

        $scope.create_document = function() {
            $http({
                method: 'POST',
                url: '../api/documents/',
                headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
                data: $.param({
                    private_number: $scope.private_number,
                    summary: $scope.summary,
                    date: $scope.date
                })
            }).success(function () {
                console.log('ok');
                $scope.get_documents();

            }).error(function(){
                alert('fail');
            });

            console.log($scope.documents)
        };


        $scope.update_document = function(document_id) {
            var obj = $.grep($scope.documents, function(e){ return e.id == document_id; })[0];

            $http({
                method: 'PUT',
                url: '../api/documents/' + document_id + '/',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},

                data: $.param({
                    private_number: obj.private_number,
                    summary: obj.summary,
                    date: obj.date
                })
            }).success(function () {
                console.log('ok');
                $scope.get_documents();
            }).error(function(){
                alert('fail');
            });

            //console.log($scope.documents)
        };

        $scope.delete_document = function(document_id) {
            $http({
                method: 'DELETE',
                url: '../api/documents/' + document_id + '/',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                data: $.param({})
            }).success(function () {
                console.log('ok');
                $scope.get_documents();
            }).error(function(){
                alert('fail');
            });

        };

        $scope.set_document_perm_can_read = function(document_id) {
            $http({
                method: 'POST',
                url: '../api/documents/' + document_id + '/set_permissions/',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},

                data: $.param({
                    user: $scope.permitUser,
                    can_read: 'true'
                })
            }).success(function () {
                //console.log('ok');
                $scope.permitUser = '';
                $scope.get_documents();
            }).error(function(){
                alert('fail');
            });
        };

        $scope.set_document_perm_can_update = function(document_id) {
            $http({
                method: 'POST',
                url: '../api/documents/' + document_id + '/set_permissions/',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},

                data: $.param({
                    user: $scope.permitUser,
                    can_update: 'true'
                })
            }).success(function () {
                //console.log('ok');
                $scope.permitUser = '';
                $scope.get_documents();
            }).error(function(){
                alert('fail');
            });
        };

        $scope.set_document_perm_can_delete = function(document_id) {
            $http({
                method: 'POST',
                url: '../api/documents/' + document_id + '/set_permissions/',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},

                data: $.param({
                    user: $scope.permitUser,
                    can_delete: 'true'
                })
            }).success(function () {
                $scope.permitUser = '';
                $scope.get_documents();
            }).error(function(){
                alert('fail');
            });
        };

}]);
