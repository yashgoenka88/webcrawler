
angular.module('app.services', [])

.service('crawlerService', ['$http', function($http){
	

	var service = {}

	service.getLinks = function(url, level){

		return $http({
		    url: '/crawl/', 
		    method: "GET",
		    params: {url: url, level:level}
		});

	}

	return service;

}])