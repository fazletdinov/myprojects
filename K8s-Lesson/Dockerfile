FROM amazonlinux

RUN yum -y update
RUN yum -y install httpd
RUN yum -y install php

COPY ./index.php /var/www/html/index.php

EXPOSE 80

CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
