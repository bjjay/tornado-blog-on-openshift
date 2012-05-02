tornado-blog-on-openshift
=========================
1.Create an account at http://openshift.redhat.com/ , and install the client tools.

2.Create a diy-0.1 application :

    rhc app create -a blog -t diy-0.1 -l email

3.Add MySQL support to your application

    rhc app cartridge add -a blog -c mysql-5.1 -l email

4.Add this upstream blog repo

    cd blog
    git remote add upstream -m master git://github.com/bjjay/tornado-blog-on-openshift.git
    git pull -s recursive -X theirs upstream master
    
5.Then push the repo upstream

    git push

6.Now,ssh into the server to init MySQL:

    ssh $(git config --get remote.origin.url | cut -d/ -f3)
    cd blog/repo/diy/
    mysql --user=$OPENSHIFT_DB_USERNAME --password=$OPENSHIFT_DB_PASSWORD --database=$OPENSHIFT_APP_NAME < schema.sql

7.That's it, you can now checkout your application at:

    http://blog-$yournamespace.rhcloud.com


NOTES:
=====

Generate ssh public key for existed openshift account:

        #create keys
        $ ssh-keygen -t rsa -f ~/.ssh/libra_id_rsa -C email  
        #add public key
        $ rhc sshkey add -i public_key_name -k ~/.ssh/libra_id_rsa.pub  -l email
        #edit your ssh config   
        $ cat ~/.ssh/config
        Host *.rhcloud.com
          IdentityFile ~/.ssh/libra_id_rsa
          VerifyHostKeyDNS yes
          StrictHostKeyChecking no
          UserKnownHostsFile ~/.ssh/libra_known_hosts
