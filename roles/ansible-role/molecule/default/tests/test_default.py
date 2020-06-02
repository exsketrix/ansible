import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ansible_installed(host):
    f = host.run('ansible --version')

    assert f.succeeded


def test_ansible_playbook_installed(host):
    f = host.run('ansible-playbook --version')

    assert f.succeeded


def test_winrm_library_exists(host):
    f = host.run('pip3 list | grep pywinrm')

    assert f.succeeded
