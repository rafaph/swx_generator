## Passos de instalação:

* Copiar os arquivos `pwk-1.0.0.tar.gz`, `simcon-1.0.6.tar.gz` e `simgph-3.3.8.tar.gz` para o diretório `/opt/simworx/releases`.

* PWK
    * Extrair o arquivo `pwk-1.0.0.tar.gz`.
    ```bash
    tar xfz pwk-1.0.0.tar.gz
    ```
    * Verificar disponibilidade da porta 3033 para o PWK ou utilizar uma nova.
        * Caso necessário, alterar a porta 3033 nos arquivos:
            * `pwk-1.0.0/conf/pwk.ini`
            * `pwk-1.0.0/deploy/pwk.conf`
    * Veficar a localização do arquivo `pocoweb.conf` e adicionar a referência para o `pwk.conf`.
        * Talvez em:
            * `/etc/nginx/conf.d/pocoweb.conf`
            * `/etc/nginx/pocoweb.conf`
        * Editar o arquivo e colocar a o caminho do `pwk.conf`.
        ```bash
        # include ...
        include /etc/nginx/includes/pwk.conf;
        ```
    * Verificar onde o arquivo `pwk.conf` deve ser colocado e copiá-lo.
        * Talvez em:
            * `/etc/nginx/includes`
    * RabbitMQ
        * Verificar se o usuário `simworx` e vhost `pwk` existem.
        ```bash
        rabbitmqctl list_user_permissions simworx
        ```
        * **Se não existir o usuário** `simworx`.
        ```bash
        rabbitmqctl add_user simworx simworx
        ```
        * **Se não existir o vhost** `pwk`.
        ```bash
        rabbitmqctl add_vhost pwk
        rabbitmqctl set_permissions -p pwk simworx ".*" ".*" ".*"
        ```
    * Criar o banco de dados `pwk`.
    ```bash
    su - postgres
    psql
    CREATE DATABASE pwk;
    \q
    exit
    ```
    * Rodar o script `install.sh` localizado em `pwk-1.0.0/deploy`.
    ```bash
    ./install.sh
    ```
    * Em caso de erro.
        * `ImportError: cannot import name scimath`.
            * Instalar a dependência `blas`.
            ```bash
            yum install -y blas
            ```
        * Demais erros que possam ocorrer.
            * Utilizar um dos comandos para procurar dependências.
            ```bash
            yum provides */<nome da dependência>
            # ou
            yum search <nome da dependência>
            ```
    * Criar o serviço `pwk`.
        * Copiar o arquivo `pwk.sh` localizado em `pwk-1.0.0/conf/pwk.sh` para `/etc/init.d/pwk`.
        ```bash
        cp pwk-1.0.0/conf/pwk.sh /etc/init.d/pwk
        ```
        * Habilitar o serviço `pwk` para inicialização com o sistema:
        ```bash
        chkconfig --level 345 pwk on
        ```
    * Reiniciar o serviço `nginx` e iniciar o `pwk`:
    ```bash
    service nginx restart
    service pwk start
    ```
* SIMCON
    * Extrair o arquivo `simcon-1.0.6.tar.gz`.
    ```bash
    tar xfz simcon-1.0.0.tar.gz
    ```
    * Parar o serviço `simcon`.
    ```bash
    service simcon stop
    ```
    * Rodar o script `install.sh` localizado em `simcon-1.0.6/deploy`.
    ```bash
    ./install.sh
    ```
    * Alterar o script do serviço do `simcon` localizado em `/etc/init.d/simcon`.
        * Na parte do comando `start` adicionar o comando taskset para os processadores 5 e 6:
    ```bash
    # antes
    # ...
    daemon $UWSGI_BIN $UWSGI_OPTIONS
    # depois
    # ...
    daemon taskset -c 5,6 $UWSGI_BIN $UWSGI_OPTIONS
    ```
    * Inicie o serviço novamente.
    ```bash
    service simcon start
    ```
* SIMGPH
    * Extrair o arquivo `simcon-3.3.8.tar.gz`.
    ```bash
    tar xfz simgph-3.3.8.tar.gz
    ```
    * Parar o serviço `simgph`.
    ```bash
    service simgph stop
    ```
    * Rodar o script `install.sh` localizado em `simgph-3.3.8/deploy`.
    ```bash
    ./install.sh
    ```
    * Alterar o script do serviço do `simgph` localizado em `/etc/init.d/simgph`.
        * Na parte do comando `start` adicionar o comando taskset para os processadores 5 e 6:
    ```bash
    # antes
    # ...
    daemon $UWSGI_BIN $UWSGI_OPTIONS
    # depois
    # ...
    daemon taskset -c 5,6 $UWSGI_BIN $UWSGI_OPTIONS
    ```
    * Inicie o serviço novamente.
    ```bash
    service simgph start
    ```

## Links para download das instalações:

[Dropbox](https://www.dropbox.com/sh/17c7nuxk8b1jdbh/AADq7lyGlAOMj2bRGN5Af9eca?dl=0)

[Google Drive](https://drive.google.com/open?id=0B3TLG2GZRMq8MHFWYU1rQW9IMkk)
