

## Задание: реализовать web приложение, используя стек библиотек языка Python

### Примеры: 
1) Записная книжка для markdown текстов (упрощенный аналог блог платформы https://telegra.ph/)
2) Чат с историей сообщений 
3) Ваш вариант


### Что должно быть использовано: 
1. Один из веб фрейморков (Flask, Django, и т.п.)
2. База данных (Redis, PostgreSQL, и т.п.)
3. Приложение должно быть оформлено в виде докер образа. 
(сборка и запуск должны выполняться **не только на вашем ноутбуке!**)

Выполненное задание нужно оформить в отдельном github репозитории. 
Ссылку на репозиторий, **с выполненной работой**, нужно прислать **до 6 ноября 23-00**. 

### Дополнительные материалы:

Установка и запуск Redis сервера:

``` bash
sudo apt-get install redis-server
pip3 install redis
```

Взаимодействие с сервером:
``` python
In [1]: import redis                                                            

In [2]: r = redis.Redis(host='localhost', port=6379, db=0)                      

In [3]: r.get('foo')                                                            

In [4]: r.set('foo', 'bar')                                                     
Out[4]: True

In [5]: r.get('foo')                                                            
Out[5]: b'bar'
```

---

Статический сайт на фласке, пример шаблонов: [https://github.com/macloo/basic-flask-app](https://github.com/macloo/basic-flask-app)

---
Работа с формами и неплохой туториал: [https://github.com/macloo/flask-forms](https://github.com/macloo/flask-forms)

---
Шпаргалка по Redis на хабре: [https://habr.com/ru/post/204354/](https://habr.com/ru/post/204354/)

---
Flask framework: [https://palletsprojects.com/p/flask/](https://palletsprojects.com/p/flask/)

---

Docker: [https://docs.docker.com/engine/docker-overview/](https://docs.docker.com/engine/docker-overview/)

---
