box= "generic/ubuntu1804"

Vagrant.configure("2") do |config|
  config.vm.provider "libvirt" do |libvirt|
    libvirt.storage_pool_name="pool"
    libvirt.driver="kvm"
    libvirt.uri="qemu:///system"
  end
  config.vm.define :Assignment do |node|
    node.vm.box = box
    node.vm.network :private_network, ip: "10.10.10.39"
    node.vm.provider "libvirt" do |d|
      d.memory = 4096
      d.graphics_type = "none"
      d.cpus = 2
  end
  config.vm.provision "shell" do |shell|
    shell.path = "docker.sh"
    end
  end
end
