# DjangoChatApp
A simple chat application built in __python's__ web framework Django using __django's__ third-party package __channels__. In this project new users have to register themselves and chat with other already registered users.



### Recommended Start
```bash
$ cd path/to/your/dev/folder
$ git clone https://github.com/sambit-git/DjangoChatApp.git
$ pip install -r requirements.txt
$ cd Chat\ Application
$ cd chatapp
$ python3 manage.py makemigrations userprofile
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
... Create the super user
```


### Install Redis
1. Download Redis
    - Using [Homebrew](http://brew.sh):
        ```
        brew install redis

        brew services start redis
        ```
        Brew permission errors? Try `sudo chown -R "$USER":admin /usr/local`

    - Direct [Download](http://redis.io/download)

2. Open & Test Redis:
    - open Terminal

    - **redis-cli ping**
        ```
        $ redis-cli ping
        PONG
        ```

    - **redis-server**
        ```
        $ redis-server
        5988:C 05 Jul 2020 23:04:24.879 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
        5988:C 05 Jul 2020 23:04:24.879 # Redis version=6.0.4, bits=64, commit=00000000, modified=0, pid=5988, just started
        5988:C 05 Jul 2020 23:04:24.879 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
                        _._                                                  
                _.-``__ ''-._                                             
            _.-``    `.  `_.  ''-._           Redis 6.0.4 (00000000/0) 64 bit
        .-`` .-```.  ```\/    _.,_ ''-._                                   
        (    '      ,       .-`  | `,    )     Running in standalone mode
        |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
        |    `-._   `._    /     _.-'    |     PID: 5988
        `-._    `-._  `-./  _.-'    _.-'                                   
        |`-._`-._    `-.__.-'    _.-'_.-'|                                  
        |    `-._`-._        _.-'_.-'    |           http://redis.io        
        `-._    `-._`-.__.-'_.-'    _.-'                                   
        |`-._`-._    `-.__.-'    _.-'_.-'|                                  
        |    `-._`-._        _.-'_.-'    |                                  
        `-._    `-._`-.__.-'_.-'    _.-'                                   
            `-._    `-.__.-'    _.-'                                       
                `-._        _.-'                                           
                    `-.__.-'                                               

        5988:M 05 Jul 2020 23:04:24.885 # Server initialized
        5988:M 05 Jul 2020 23:04:24.885 * Ready to accept connections

        ```
        **Close Redis** with `control` + `c` to quit