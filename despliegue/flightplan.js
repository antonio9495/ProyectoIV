var plan = require('flightplan');

plan.target('despliegue', [
 {
	host: '35.241.153.196',
	username: 'antonio',
	agent: process.env.SSH_AUTH_SOCK
}]);

plan.remote(['exec'], function(remote){
	remote.log('Executing server...');
	remote.with('cd ~/ProyectoIV/', function(){
		remote.exec('sudo gunicorn application:app -b 0.0.0.0:80');
	});
});

plan.remote(['kill'], function(remote){
	remote.log('Stop server...');
	remote.with('cd ~/ProyectoIV/', function(){
		remote.exec('sudo gunicorn application:app -b 0.0.0.0:80');
	});
});