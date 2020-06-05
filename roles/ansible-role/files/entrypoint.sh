#!/bin/bash
set -e

if [[ -v LOCAL_USER_ID ]]; then

  echo "Starting with UID : $LOCAL_USER_ID"
  useradd --shell /bin/bash -u $LOCAL_USER_ID -o -c "" -m user -g root
  export HOME=/home/user
  exec /usr/local/bin/gosu user "$@"
else
  useradd -m ansible -g root
  export HOME=/home/ansible
  exec /usr/local/bin/gosu ansible "$@"
fi