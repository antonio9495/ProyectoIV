# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "google/gce"

  config.vm.provider :google do |google, override|
    google.google_project_id = "composed-hash-231317"
    google.google_client_email = "proyectoiv@composed-hash-231317.iam.gserviceaccount.com"
    google.google_json_key_location = "~/claves/composed-hash-231317-0517472e5457.json"
    google.image_family = 'ubuntu-1604-lts'
    google.machine_type = 'n1-standard-1'
    google.name = 'practica-iv'
    google.zone = "europe-west1-b"
    google.tags = ['http-server']
    override.ssh.username = "antonio"
    override.ssh.private_key_path = "~/claves/id_rsa"
  end
  config.vm.provision :ansible do |ansible|
        ansible.become = true
        ansible.verbose = "vvvv"
        ansible.playbook = "./provision/playbook.yml"
  end
end