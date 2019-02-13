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
		remote.exec('sudo gunicorn application:app -b 0.0.0.0:80 2> /tmp/execution.log');
	});
});

plan.remote(['kill'], function(remote){
	remote.log('Stop server...');
	remote.exec('sudo kill -9 `ps aux |grep gunicorn |grep application | awk \'{ print $2 }\'` 2> /tmp/kill.log');
});

plan.local(['logs'], function(local) {
  local.log('Copy log files from remote hosts');
  local.exec('gcloud compute scp --recurse practica-iv:/tmp ~/remoteLogs --zone europe-west1-b')
});