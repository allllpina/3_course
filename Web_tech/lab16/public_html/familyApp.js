var app = angular.module('familyApp', []);

app.controller('familyCtrl', function($scope) {
  $scope.user = {};
  $scope.cards = [];

  $scope.submitForm = function () {
    if ($scope.registerForm.$valid) {
      // Перевірка типів даних перед додаванням користувача
      if (
        angular.isString($scope.user.gender) &&
        angular.isString($scope.user.age) &&
        angular.isString($scope.user.surname) &&
        angular.isString($scope.user.name) &&
        angular.isString($scope.user.login) &&
        angular.isString($scope.user.password) &&
        angular.isString($scope.user.email) &&
        (angular.isUndefined($scope.user.question) || angular.isString($scope.user.question)) &&
        angular.isString($scope.user.interest)
      ) {
        // Якщо типи правильні, додаємо копію даних
        $scope.cards.push(angular.copy($scope.user));
  
        // Очищаємо форму
        $scope.user = {};
        $scope.registerForm.$setPristine();
        $scope.registerForm.$setUntouched();
      } else {
        alert("Помилка типів даних! Перевірте заповнені поля.");
      }
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
