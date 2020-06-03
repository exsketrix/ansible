# Ansible Docker Image

# How to run this docker image:

```shell
    docker run -it --rm -v /var/run/docker.sock:/var/run/docker.sock -v ${PWD}:/ansible-playbook exsketrix/ansible:<ansible_version> <ansible_cmd> <ansible_playbook_args>
```

Example execution:

```shell
    docker run -it --rm -v /var/run/docker.sock:/var/run/docker.sock -v ${PWD}:/ansible-playbook exsketrix/ansible:2.9.9 ansible-playbook -i /ansible-playbook/inventory /ansible-playbook/run_playbook.yml
```

# Test and Development Lifecycle:

The following steps provide the basis for a continual test, develop and build lifecycle of this image:

1) Before making modifications to the Dockerfile in 'roles/ansible-role/templates/Dockerfile.j2', consider whether any changes that need to be made can be verified using testinfra. If this is the case, first go into 'roles/ansible-role/molecule/default/tests/test_default.py' and update and/or add further tests.

2) Execute molecule to confirm test failures.

```shell
    cd roles/ansible-role
    docker run --rm -it \
        -v "$(pwd)":/tmp/$(basename "${PWD}"):rw \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -w /tmp/$(basename "${PWD}") \
        quay.io/ansible/molecule:3.0.3 \
        molecule test
```

3) Update 'roles/ansible-role/templates/Dockerfile.j2' with modifications required that will address the test verification changes. Execute the playbook to re-build the docker image.

```shell
    ansible-playbook -i inventory create-docker-image.yml
```

4) Re-run molecule test to verify all tests including modified/additional test verifications now pass.

```shell
    cd roles/ansible-role
    docker run --rm -it \
        -v "$(pwd)":/tmp/$(basename "${PWD}"):rw \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -w /tmp/$(basename "${PWD}") \
        quay.io/ansible/molecule:3.0.3 \
        molecule test
```

Refer to the official [TestInfra Modules API](https://testinfra.readthedocs.io/en/latest/modules.html) for the complete set of functions that can be tested.