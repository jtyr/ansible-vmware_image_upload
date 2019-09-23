vmware_image_upload
===================

Ansible role which helps to upload VM image to VMware vCenter.

The configuration of the role is done in such way that it should not be
necessary to change the role for any kind of configuration. All can be
done either by changing role parameters or by declaring completely new
configuration as a variable. That makes this role absolutely
universal. See the examples below for more details.

Please report any issues or send PR.


Examples
--------

```yaml
---

- name: Example of how to upload VM image to vCenter
  hosts: vcenter-servers
  connection: local
  gather_facts: no
  vars:
    vmware_image_upload_username: mydomain\\myuser
    vmware_image_upload_password: MyT0pS3cr3tP4Sw0rd!
    vmware_image_upload_datacenter: MYDC1
    vmware_image_upload_cluster: mycluster
    vmware_image_upload_datastore: datastore1
    vmware_image_upload_network: mynet
    vmware_image_upload_folder: /{{ vmware_image_upload_datacenter }}/vm/Templates
    vmware_image_upload_name: Golden-VMware-CentOS-7-1567778833
    vmware_image_upload_ovf: /path/to/the/{{ vmware_image_upload_name }}.ovf
  roles:
    - role: vmware_image_upload
      tags: vmware_image_upload
```


Role variables
--------------

```yaml
# vCenter hostname
vmware_image_upload_hostname: "{{ ansible_host }}"

# vCenter port number
vmware_image_upload_port: 443

# Whether to validate SSL certificates
vmware_image_upload_validate_certs: no

# Reguired variables which must be specified by the user
vmware_image_upload_username: null
vmware_image_upload_password: null
vmware_image_upload_name: null
vmware_image_upload_datacenter: null
vmware_image_upload_cluster: null
vmware_image_upload_datastore: null
vmware_image_upload_folder: null
vmware_image_upload_network: null
vmware_image_upload_networks: "{u'VM Network':u'{{ vmware_image_upload_network }}'}"
vmware_image_upload_ovf: null

# Set to 'absent' to delete the uploaded image
#vmware_image_upload_state: null
```


License
-------

MIT


Author
------

Jiri Tyr
