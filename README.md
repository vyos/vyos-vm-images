# vyos-vm-images

[Ansible](https://www.ansible.com/) playbooks to build VyOS VM images.

## Supported Platforms

- QEMU

    ```
    ansible-playbook -i hosts qemu.yml
    ```

- VMware

    ```
    ansible-playbook -i hosts vmware.yml
    ansible-playbook -i hosts vmware.yml -e vyos_vmware_private_key_path=path_to_private_key
    ```

- Microsoft Hyper-V

    ```
    ansible-playbook -i hosts hyperv.yml
    ```

- Vagrant libvirt

    ```
    ansible-playbook -i hosts vagrant-libvirt.yml
    ```
