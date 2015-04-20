# kibana4-rpm
RPM spec file and init script for CentOS 6 and Kibana 4.  Requires daemonize and elasticsearch.

To enable the repositoties see the links below.
https://fedoraproject.org/wiki/EPEL
http://www.elastic.co/guide/en/elasticsearch/reference/current//setup-repositories.html

Once enabled:
$ sudo yum install elasticsearch daemonize
$ sudo rpm -ivh kibana-4.0.2-1.el6.x86_64.rpm

