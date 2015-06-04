(function (){
  'use strict';
  angular.module('tickets', ['ngResource', 'ngRoute']);

  function config($locationProvider, $httpProvider, $routeProvider) {
    $locationProvider.html5Mode(true);

    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';

    $routeProvider
      .when('/tickets', {
        templateUrl: 'static/tickets/views/tickets.html'
      })
      .otherwise({
        redirectTo: '/'
      });
  }

  angular.module('tickets').config(config);

  function authState(){
    return {user: undefined};
  }

  angular.module('tickets').service('authState', authState);

  function api($resource){
    function add_auth_header(data, headersGetter){
        var headers = headersGetter();
        headers['Authorization'] = ('Basic ' + btoa(data.username +
                                    ':' + data.password));
      console.log(headers['Authorization']);
    }
    return {
        auth: $resource('/api/auth\\/', {}, {
            login:  {method: 'POST', transformRequest: add_auth_header},
            logout: {method: 'DELETE'}
        }),
        usuarios: $resource('/api/usuarios\\/', {}, {
            create: {method: 'POST'}
        }),
        tickets: $resource('/api/tickests\\/', {}, {
            list:   {method: 'GET', isArray: true},
            create: {method: 'POST'},
            detail: {method: 'GET', url: '/api/tickets/:id'},
            delete: {method: 'DELETE', url: '/api/tickets/:id'}
        }),
      respuestas: $resource('/api/respuestas\\/', {}, {
            list:   {method: 'GET', isArray: true},
            create: {method: 'POST'},
            detail: {method: 'GET', url: '/api/respuestas/:id'},
            delete: {method: 'DELETE', url: '/api/respuestas/:id'}
      })
    };
  }
  angular.module('tickets').factory('api', api);

  function authController($scope, api, authState) {
    // $('#id_auth_form input').checkAndTriggerAutoFillEvent();

     $scope.authState = authState;

     $scope.getCredentials = function(){
         return {username: $scope.username, password: $scope.password};
     };
     $scope.login = function(){
         console.log($scope.getCredentials());
         api.auth.login($scope.getCredentials()).
             $promise.
                 then(function(data){
                     authState.user = data.username;
                     $scope.PerfilUsuario = data;
                 }).
                 catch(function(data){
                     alert(data.data.detail);
                 });
     };
     $scope.logout = function(){
         api.auth.logout(function(){
             authState.user = undefined;
         });
     };
     $scope.register = function($event){
         $event.preventDefault();
         api.users.create($scope.getCredentials()).
             $promise.
                 then($scope.login).
                 catch(function(data){
                     alert(data.data.username);
                 });
     };
  }

  angular.module('tickets').controller('authController',authController);

})();
