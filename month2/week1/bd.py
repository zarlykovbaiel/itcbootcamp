5# -- \C KYRGYZSTAN
# Заголовок: "KYRGYZSTAN".

# --  CREATE TABLE developers(
# --    id SERIAL PRIMARY KEY,
# --    name VARCHAR,
# --    population INT
   
# -- );

# --  INSERT INTO developers(
# --  name,
# --  population
# --  )
# --   VALUES(
# --    'Naryn', 300000
# --  );

# ДОБАВЛЕНИЕ НОВОЙ КОЛОНКИ
# -- ALTER TABLE developers ADD COLUMN teams VARCHAR;

# ПЕРЕИМЕНОВАНИЕ
# -- ALTER TABLE developers RENAME COLUMN population TO participants;

# УДАЛЕИЕ
# DELETE FROM developers WHERE participants = 300000;

# -- create table red(
# -- id serial primary key,
# --   name VARCHAR(255) NOT NULL,
# --   age INT default 18,
# --   hobbi VARCHAR default 'football'
# -- );
# -- select * from red;
# COMMENT ON table rim IS 'ну русский язык'



# Vladimir, [25.08.21 21:20]
# -- INSERT INTO developers(
# -- name,
# -- skill
# -- )
# -- VALUES()
# -- 'Bob',
# -- 'SuperBoss'
# -- );
#  -- select * from developers;

#  -- DELETE FROM developers WHERE id = 12;
#  ИЗМЕНЕНИЯ ЗНАЧЕНИЯ
# UPDATE cars SET name = 'MB' WHERE country = 'GERMANY';

#  -- UPDATE developers SET name ='Bektur' WHERE name ='Dinara';

#  -- UPDATE developers SET name ='Vladimir' WHERE id=1;

# -- UPDATE developers SET name ='Vladimir' WHERE id=1 or id=4;

#  -- UPDATE developers SET id=2 WHERE id=13;

# Vladimir, [25.08.21 21:20]
# -- CREATE TABLE develops(
# -- id SERIAL PRIMARY KEY,
# -- name VARCHAR(255) NOT NULL,
# -- age INT,
# -- hobby VARCHAR DEFAULT 'Basketball'
# -- );
#  -- INSERT INTO develops(
# -- name,
# -- age
# -- ) VALUES(
# -- 'John',
# -- 23);

#  -- коммент
# -- COMMENT ON table develops IS 'Хай бро';

#  -- удаление и добавление колонн
# -- ALTER TABLE develops ADD COLUMN female VARCHAR;
# -- ALTER TABLE develops DROP COLUMN female;

#  -- изменить имя колонки
# -- ALTER TABLE develops RENAME COLUMN hobby TO favorite;

# --просмотр
#  -- select * from develops;

# Считает количество строк которые подходят под
# условияи не имеют NULL
# select COUNT(*) from users

# ОТСОРТИРОВАТЬ БОНУСНЫМ СПОСОБОМ
# SELECT * FROM users WHERE LOGIN ~'(as|cd|gp)';


# SQL можно читать 2 и более
# Таблицы одновременнно.
# SELECT login,followers FROM users WHERE followers = (SELECT max(followers) FROM users);

# Напишите запрос, который выводит всю информацию самого знаменитого пользователя
# SELECT * FROM users WHERE followers = (SELECT max(followers) FROM users);



# Найдите среднее количество подписчиков
# SELECT AVG (followers) FROM users;

# 5. Отсортируйте всех пользователей по логину
# SELECT * FROM users ORDER BY login;

# 6. Отсортируйте всех пользователей по стране
# SELECT * FROM users ORDER BY COUNTRY;


# 7. Отсортируйте всех пользователей по email
# SELECT * FROM users ORDER BY email;


# 8. Напишите запрос,который выводит id из колонки пользователей и имя из колонки clients
# SELECT user_id, login FROM users;


# 9. Напишите запрос,который выводит всё о пользователе, чей логин содержит as, cg, si, am, qwe, er, ka, an
# SELECT login FROM users WHERE LOGIN ~'(as|cg|si|am|qwe|er|ka|an)';


# 10. Напишите запрос,который выводит всё о пользователе, чей логин заканчивается на lol, kan, ck, ie. ig
# SELECT login FROM users WHERE login LIKE '%lol' OR login LIKE '%ken'OR login LIKE '%ck'OR login LIKE '%ie' OR login LIKE '%ig';

# 11. Напишите запрос, который выводит всё о пользователе, чей логин начинается на a, b, c, d, M, D, A
# SELECT login FROM users WHERE login LIKE '%a' OR login LIKE '%b'OR login LIKE '%c'OR login LIKE '%d' OR login LIKE '%M'  OR login LIKE '%D' OR login LIKE '%A';

# 12. 12.Как зовут самого знаменитого Сеньор Программиста(Senior Programmer) из Израиля(Israel)?
# SELECT * FROM users  WHERE profession = 'Senior Programmer' AND country = 'China' ;



# 1. Выведите на экран всех пользователей у кого пустая почта.
# SELECT * FROM users  WHERE email = '';

# 2. Посчитайте сколько пользователей у которых нет email живут на Chui.
# SELECT * FROM users  WHERE email = '' AND address = 'Manasa 102';
# 3. Покажите имена и номера телефонов всех людей которые работают как Web Developer
# SELECT login,phone_number FROM users  WHERE profession = 'Web Developer';

# 4. У всех пользователей у которых почта ровняется False обновите почту на user@gmail.com.
# UPDATE users SET email = 'user@gmail.com' WHERE email = '';

# 5. Узнайте из каких стран люди которые не имеют работы(Unemployed).


# 6. Везде где номер телефона начинается с 000 замените его любой РЕАЛЬНЫЙ номер в формате
# столбца phone_number.
# UPDATE users SET phone_number = '+996708262674' WHERE phone_number LIKE '000%';



# 7. 12345, user123б, qwerty считается лёгкими паролями у каждого пользователя у кого лёгкий
# пароль удалите из Базы Данных.
# DELETE FROM users  WHERE password ~'(12345|user1236|qwerty)';



# 8. Выведите на экран email всех .NET Developer разработчиков и отсортируйте их по Имени.
# SELECT login,email FROM users WHERE profession = '.NET Developer' ORDER BY login;
