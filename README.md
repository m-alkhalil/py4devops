This Python script:
    - Use resquest package to fetch weather data from weather api at teh beginning of 3 hours period for 5 days
    - use configparser tp pars API key from the config file config.ini
    - Use logging to log the data and store it into a log file



Future updates:
    - Implement authentication
    - store api key in environment varialbes and read it from there


py logging has loggers
    loggers cnsist of Handlers  Formatters and filters (log Records and LoggerAdapter)
        - Handler defines where log messages get commited to: File, Console, endpoint
            - Default handlers: SMTPHandler for email notifications
                                HTTPHandler use basic authorization header to connect to another web server
                                RotatingFileHandler
                                TimeRotatingFileHandler
                                SysLogHandler
                                QueueHandler
                                StreamHandler: default, it putputs to sys.stdout and sys.stderr  

        - Log Levels:  30 is in both prod and dev, CUSTOM levels can be created but not recomended
                CRETICAL 50
Produciton      ERROR    40
                Warning  30 
DEV&STAG        INFO     20
                DEBUG    10
                NOSET    00  .. kept switched off  

        - Formatters:
            - defins how messages are structured and how he information are output, as if and how timestamp is shown 
                in front of the message. 
            - a loth of placeholders are thre to use, and it can be created too when modifying th elog record object. 

        - Configurations: 2 methods
            -  dictionary configuration, basi logging
            - configuraiton file: .Yaml, .ini 

             