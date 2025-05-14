var app = angular.module('familyApp', []);

app.controller('familyCtrl', function($scope) {
  $scope.user = {};
  $scope.cards = [];

  $scope.submitForm = function () {
    if ($scope.registerForm.$valid) {
      // Додаємо копію введених даних до списку
      $scope.cards.push(angular.copy($scope.user));

      // Очищаємо форму
      $scope.user = {};
      $scope.registerForm.$setPristine();
      $scope.registerForm.$setUntouched();
    }
  };

  $scope.resetForm = function() {
    $scope.user = {
      email: 'example@email.com'
    };
    // Якщо форма вже була заповнена, ми її "перезапускаємо"
    $scope.registerForm.$setPristine();
    $scope.registerForm.$setUntouched();
  };
  

});
