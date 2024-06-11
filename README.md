# NewWaveEducation
Онлайн платформа для самообразования

## Техническое задание проекта 

- [ ] Реализовать функционал самообучения для студентов. 

- [ ]Для этого необходимо создать платформу, которая работает только с авторизованными пользователями.

- [ ] На платформе необходимо предусмотреть функционал разделов и материалов. 

- [ ] Для каждого материала можно добавить тесты.

- [ ] Управление всеми сущностями необходимо реализовать через стандартный Django admin.

- [ ] Проверка ответа на тест осуществляется с помощью отдедльного запроса на бэкенд. 

- [ ]Реализовать либо Rest API, либо SSR с использованием Bootstrap.

- [x] Для реализации проекта использовать фреймворк Django.

## Используемые технологии 

1. PostgreSQL 
2. ORM 
3. Serializers 
4. Viewset/Generics 
5. Filter 
6. Cors 
7. Tests 
8. Git 
9. Readme 
10. PEP8 
11. Swagger 

## Детали реализации 

- [ ] Авторизация пользователей (приложение Users)
- [ ] Приложение Courses c моделями разделов и материлов 
- [ ] Приложение Tests, с моделями вопросов и ответов по материалам
- [ ] Регистрация всех сущностей в административной панели
- [ ] База в PostgreSQL
- [ ] Использованы сериалайзеры
- [ ] Использованы Viewset/Generic
- [ ] Использованы фильтры
- [ ] Использован CORS
- [x] Создано Readmi 
- [x] Проект выложен на GitHub
- [ ] Проект соответствует PEP 8 
- [ ] Создана документация Swager 

## Развёртывание проекта 
1. Склонируйте репозиторий 
```sh
git clone https://github.com/AndrewSkow11/NewWaveEducation
```
2. Создайте виртуальное окружение и активруйте его
```sh
python3 -m venv venv
source venv/bin/activate
```

3. Установите зависимости из файла requirements.txt

4. Примените миграции 

5. Запустие проект