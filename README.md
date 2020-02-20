# vyos-vm-images

[Ansible](https://www.ansible.com/) playbooks to build VyOS VM images.

## Requirements

You need a machine with at least 20 GB free space with Debian 10 (bare-metal, virtual, Docker container with --privileged flag). Also, you need to install ansible and python packages:

```
sudo apt update
sudo apt install -y ansible python
```

All other requirements will be installed by ansible-playbook.


## Prepare

You need to copy the ISO image with VyOS to /tmp/vyos.iso before running ansible-playbook. Resulting images also will be located inside /tmp/ directory.

## Supported Platforms

- QEMU

    ```
    ansible-playbook qemu.yml
    ```

- VMware

    ```
    ansible-playbook vmware.yml
    ansible-playbook vmware.yml -e vyos_vmware_private_key_path=path_to_private_key
    ```

- Microsoft Hyper-V

    ```
    ansible-playbook hyperv.yml
    ```

- Vagrant libvirt

    ```
    ansible-playbook vagrant-libvirt.yml
    ```

## Additional (optional) parameters

- Path to local ISO image (default: /tmp/vyos.iso):

    ```
    -e iso_local=path
    ```

    Example:

    ```
    -e iso_local=/tmp/vyos/custom_image.iso
    ```

- Disk size (default: 10GB):

    ```
    -e disk_size=size
    ```

    Example for 2 GB:

    ```
    -e disk_size=2
    ```

- Enable Cloud-init (default: according to platform):

    ```
    -e cloud_init=true
    ```

- Configure custom Cloud-init datasources (default: according to platform):

    ```
    -e cloud_init_ds=datasources
    ```

    Example:
    ```
    -e cloud_init_ds=NoCloud,ConfigDrive,None
    ```
