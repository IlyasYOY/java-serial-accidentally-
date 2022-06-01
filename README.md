# Простой пример машины, которая не может

Для работы надо: 
- **SDKman**
- **Python3** 
- **Java** (8,11, 17)
- **Docker**

Ручками надо собрать для каждой версии **Java**

```shell 
sdk use java 11 # Или какая у вас там версия
gradle build # ./app/build.gradle надо поменять javaVersion
```

[Ссылка](app/build.gradle) на `build.gradle`.

Так делаете для каждой из версий: 8, 11, 17.

Далее копируйте все **JAR** в корень:

```shell 
cp app/build/libs/app* .
```

Потом собирайте все **Dockerfile**:

```shell 
python3 build_all_dockers.py
```

Запускаете контейнер из того образа, что ближе для души: 

```bash 
docker run -m 2000MB --cpus=2 java-11-test # Не Serial
docker run -m 1000MB --cpus=1 java-11-test # Serial
```

Подробнее можно почитать [тут](https://habr.com/en/company/hh/blog/450954/).
