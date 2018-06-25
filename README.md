# vyos-vm-images

[Ansible](https://www.ansible.com/) playbooks to build VyOS VM images.

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
