angular.module('familyApp', []).controller('familyCtrl', function ($scope) {
    $scope.family = [
        { id: 1, firstName: 'Олександр', lastName: 'Іваненко', age: 35, gender: 'Чоловіча', role: 'Батько' },
        { id: 2, firstName: 'Марина', lastName: 'Іваненко', age: 32, gender: 'Жіноча', role: 'Мати' },
        { id: 3, firstName: 'Артем', lastName: 'Іваненко', age: 10, gender: 'Чоловіча', role: 'Син' },
        { id: 4, firstName: 'Олена', lastName: 'Іваненко', age: 8, gender: 'Жіноча', role: 'Донька' },
        { id: 5, firstName: 'Богдан', lastName: 'Коваленко', age: 60, gender: 'Чоловіча', role: 'Дідусь' },
        { id: 6, firstName: 'Людмила', lastName: 'Коваленко', age: 58, gender: 'Жіноча', role: 'Бабуся' },
        { id: 7, firstName: 'Ігор', lastName: 'Петренко', age: 40, gender: 'Чоловіча', role: 'Дядько' },
        { id: 8, firstName: 'Наталія', lastName: 'Петренко', age: 38, gender: 'Жіноча', role: 'Тітка' },
        { id: 9, firstName: 'Василь', lastName: 'Сидоренко', age: 50, gender: 'Чоловіча', role: 'Хрещений' },
        { id: 10, firstName: 'Ганна', lastName: 'Сидоренко', age: 48, gender: 'Жіноча', role: 'Хрещена' }
    ];

    $scope.roles = ['Батько', 'Мати','Син','Донька','Дідусь','Бабуся','Дядько','Тітка','Хрещений', 'Хрещена']
    
    $scope.hideform = true;
    $scope.sortColumn = '';

    $scope.sortBy = function (column) {
        $scope.sortColumn = column;
    };

    $scope.editMember = function (id) {
        $scope.hideform = false;
        if (id === 'new') {
            $scope.isNew = true;
            $scope.firstName = '';
            $scope.lastName = '';
            $scope.age = '';
            $scope.gender = 'Чоловіча';
            $scope.role = '';
        } else {
            $scope.isNew = false;
            let member = $scope.family.find(m => m.id === id);
            $scope.firstName = member.firstName;
            $scope.lastName = member.lastName;
            $scope.age = member.age;
            $scope.gender = member.gender;
            $scope.role = member.role;
            $scope.currentIndex = $scope.family.indexOf(member);
        }
    };

    $scope.saveMember = function () {
        if ($scope.isNew) {
            let newId = $scope.family.length + 1;
            $scope.family.push({
                id: newId,
                firstName: $scope.firstName,
                lastName: $scope.lastName,
                age: $scope.age,
                gender: $scope.gender,
                role: $scope.role
            });
        } else {
            let member = $scope.family[$scope.currentIndex];
            member.firstName = $scope.firstName;
            member.lastName = $scope.lastName;
            member.age = $scope.age;
            member.gender = $scope.gender;
            member.role = $scope.role;
        }
        $scope.hideform = true;
    };
});
