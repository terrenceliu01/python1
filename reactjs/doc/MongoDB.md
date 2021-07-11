# MongoDB Installation Process

## Download MongoDB Installation File
* Windows 10 OS
[download website](https://www.mongodb.com/try/download/community?tck=docs_server)

![Download Webpage](images/DownloadWebPage.png)

Download File Name: mongodb-windows-x86_64-4.4.1-signed.msi

* Mac OS
[download website](https://www.mongodb.com/try/download/community)
![Download Webpage](images/DownloadPage4Mac.png)

Download File Name: mongodb-macos-x86_64-4.4.1.tgz

## Install MongoDB on Windows 10
* Run the download file above in Downloads folder

![Step0](images/mongodb0.png)

![Step1](images/mongodb1.png)

![Step2](images/mongodb2.png)

![Step3](images/mongodb3.png)

![Step4](images/mongodb4.png)

![Step5](images/mongodb5.png)

![Step6](images/mongodb6.png)

![Step7](images/mongodb7.png)

## Issue on Catalina 
MongoDB need create a data folder on root /data/db, but Catalina on Mac does not allow to generate folder on root for security reason.
the following is work around by create a config file named mongod.conf.

* Fix Catalina /data/db issue
```
mkdir /usr/local/var/log/mongodb
mkdir /usr/local/var/mongodb
copy mongod.conf > /usr/local/etc
mongod --config /usr/local/etc/mongod.conf
```

* following is the content in mongod.conf file.
```conf
systemLog:
  destination: file
  path: /usr/local/var/log/mongodb/mongo.log
  logAppend: true
storage:
  dbPath: /usr/local/var/mongodb
net:
  bindIp: 127.0.0.1
```

* another way to install mongodb on MacOS.

```
brew tap mongodb/brew
brew install mongodb-community@4.2
```
