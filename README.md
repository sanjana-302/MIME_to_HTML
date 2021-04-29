# MIME_to_HTML
A python script to save emails in html format from MIME(EML) standard to local system.

This script reads Standard MIME RFC 822 from your inbox and converts in into HTML format. This then automatically saves into system. 

## How to use ?

```sh
    Clone this repository.
```
```sh
    Install requirements.
```
```sh
    python email_write.py
```

Currently, this saves all emails from "inbox" to a directory called "email" in your system (this will be created in same working directory where you run script).

## How are subdir(s) named in "email" ?

The latest email will be fetched first and it's subdir name will be binary form for decimal number 1 , it keeps incresing for subsequent emails. This can be easily changed as required.

## How to view my emails locally ?

Just go to subdir , you will find html file , click on it.
You are good to go!
