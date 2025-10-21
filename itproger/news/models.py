from django.db import models

class Articles(models.Model):
  title = models.CharField('Название', max_length=50)
  anons = models.CharField('Анонс', max_length=250)
  full_text = models.TextField('Статья')
  date = models.DateTimeField('Дата публикации')

  def __str__(self): # Отображает строку, вместо object(num)
    return self.title
  
  class Meta: # Позволяет изменять имя таблицы в БД  db_table, ordering(сортировка), удобночитаемые имена (verbose_name)
    verbose_name = 'Новость'
    verbose_name_plural = 'Новости'
  # db_table = 'custom_table_name';

"""
Типы полей:
1. CharField('field_name', max_length=) - Для коротких текстовых строк
2. TextField('field_name')              - Для больших текстовых блоков
3. IntegerField()                       - Для целых чисел
4. PositiveIntegerField()               - Только положительные целые числа(включая 0)
5. SmallIntegerField()
6. BigIntegerField()
7. DecimalField()                       - Для точных десятичных чисел
                                        - Обязательные параметры: max_digits, decimal_places
8. FloatField()                         - Числа с плавающей точкой
9. DateField()                          - Только дата (год, месяц, день)
                              auto_now_add=True - устанавливается при создании
                              auto_now=True - обновляется при каждом сохранении
10. DateTimeField()                     - Дата и время
11. TimeField()                         - Только время (часы, минуты, секунды)
12. BooleanField()                      - True/False значения
13. FileField()                         - Для загрузки файлов
                                        - Обязательный параметр upload_to
14. ImageField()                        - Для изображений (требует Pillow)

avatar = models.ImageField(
    upload_to='avatars/',
    height_field='image_height',
    width_field='image_width'
)

15. SlugField()                         - Для URL-адресов, идентификаторов
                          - Содержит только буквы, цифры, дефисы и подчеркивания

# Тестовая модель
class Category(models.Model):
  name = models.CharField(max_length=100, db_index=True) # Индексируемое поле
  slug = models.SlugField(max_length=255, unique=True, db_index=True) 
  # Уникальное поле

  def __str__(self): # Отображает строку, вместо object(num)
    return self.name

class Main(models.Model):
  ...
  ...
  cat =  models.ForeignKey('Category', on_delete=models.PROTECT) 
  # Протект, тк не будут удаляться поля, связанные с этой моделью.

Связи между моделями:

1. ForeignKey()                         - Many to One
                          CASCADE - удалить связанные объекты
                          PROTECT - запретить удаление
                          SET_NULL - установить NULL
                          SET_DEFAULT - установить значение по умолчанию
                          DO_NOTHING - удаление записи у первичной модели не вызывает никаких действий у вторичных моделей

user = models.ForeignKey(
    User, # class
    on_delete=models.CASCADE
)
category = models.ForeignKey(
    'Category',
    on_delete=models.PROTECT
)

2. OneToOneField()                        - One to One
Пример: Гражданин и его ИНН, т.е. только у одного поля A может быть только одно поле B.

3. ManyToManyField()                      - Many to Many
                                          - Создает промежуточную таблицу
Пример студенты и преподаватели. У студента может быть множество преподавателей и у преподавателя множество студентов.

"""