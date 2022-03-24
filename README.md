<h2>Запуск</h2>
<code>python manage.py runserver</code>

<h3>Фикстуры создавались скриптом</h3>
<code>python createfixtures.py</code><br>
*Добавляем города из фикстур*<br>
<code>python manage.py loaddata addcities.json
</code><br>
*Добавляем людей из фикстур*<br>
<code>python manage.py loaddata addpeople.json
</code><br>
Миграции<br>
<code>python manage.py makemigrations
</code><br>
<code>python manage.py migrate
</code><br>
Старт сервера<br>
<code>python manage.py runserver</code>

*Эндпоинты*:<br>
admin/ - стандартная админка, логин и пароль - admin <br>
main - главная страница  <br>
citypage/<int:pk> - страница отображения информации по городу<br>
city/<int:pk> - может отработать get запрос для получения названия города и списка его жителей<br>


ClearState можно раскомментировать и использовать для полной очистки базы, однако при пересоздании через фикстуры необходимо будет также обнулить инкреминтатор в БД.
<br>
**Отправляю с заполненными фикстурами и БД**

