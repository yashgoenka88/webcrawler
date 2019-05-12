
angular.module('app.controllers', [])

.controller('mainController', ['$rootScope','crawlerService','$interval', function($rootScope, crawlerService, $interval){
	
	var self = this;

	self.url = ''
	self.level = ''

	var apiTimer = 0


	self.getLinks = function(url, level){

		var success = function(res){

			self.data = res.data

			self.fetching = false

		}

		var failure = function(res){

			self.error = res.data.msg

			self.fetching = false

		}

		self.error  = null

		self.data = null

		self.fetching = true

		if(level > 2){
			self.loadertext = 'Releasing the spiders on ' + url+ ' ,this may take upto 10 minutes ..'	
		}else{
			self.loadertext = 'Releasing the spiders on ' + url+ ' ,this may take a few minutes ..'
		}

		crawlerService.getLinks(url, level).then(success, failure)
	}


}])