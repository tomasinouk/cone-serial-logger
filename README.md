# cone-serial-logger
>Warning: **Work in progress**

Works in conjunction with XC-RS232 module installed or USB/Serial plugged in.

Com port is configured as TCP-Server.

Script is acting as a TCP-Client and receiving data received on physical com port. 

Conel User module/s: 

* Python user user module.

Conel Configuration snippet:

```
PORT_ENABLED=1
PORT_BAUDRATE=9600
PORT_DATABITS=8
PORT_PARITY=N
PORT_STOPBITS=1
PORT_SPLIT=20
PORT_PROTO=tcp
PORT_MODE=server
PORT_IPADDR=
PORT_PORT=4001
PORT_INACT_TIME=
PORT_REJECT_NEW=0
PORT_KEEPALIVE=0
PORT_KEEPALIVE_TIME=3600
PORT_KEEPALIVE_INTVL=10
PORT_KEEPALIVE_PROBES=5
PORT_USE_CD=0
PORT_USE_DTR=0
``` 