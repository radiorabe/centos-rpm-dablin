#!/bin/bash
#
# RPM build wrapper for dablin, runs inside the build container on travis-ci

set -xe

curl -o /etc/yum.repos.d/dab.repo https://download.opensuse.org/repositories/home:/radiorabe:/dab/CentOS_7/home:radiorabe:dab.repo

yum -y install \
    epel-release \
    http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm

chown root:root dablin.spec

build-rpm-package.sh dablin.spec
