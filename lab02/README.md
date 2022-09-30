# Как использовать

Общая справка:

```bash
python3 main.py -h
```

Справка по режимам, например:

```bash
python3 main.py str -h
```

# Демонстрация

Шифрование:

```bash
python3 main.py bin data/Secret.pdf --out JustAFile.pdf
```

Результат (если вылетает ошибка, создайте директорию `config`):

```
Файл зашифрован и сохранен под именен JustAFile.pdf!
Настройки Энигмы успешно сохранены в файл config/bin
```

Попробовать открыть:

```bash
xdg-open JustAFile.pdf
```

Результат `ошибка чтения файла`.

Для расшифровки нужны начальные настройки Энигмы при шифровании, сохраненные,
как показано выше, в `config/bin`:

```bash
python3 main.py bin JustAFile.pdf --conf config/bin --out Result.pdf
```

Результат:

```bash
Настройки Энигмы успешно загружены из файла config/bin
Файл зашифрован и сохранен под именен Result.pdf!
```

Файл `Result.pdf` должен открыться:

```bash
xdg-open Result.pdf 
```

# Как это работает

Кратко:

1. Энигма состоит из коммутационной панели (в данной лабе не реализовывалась),
   роторов (обычно 3, были Энигмы и с большим числом) и рефлектора.

2. На коммутационной панели буквы соединялись парами (возможно, соединялись
   только некоторые буквы). Соединенные буквы менялись местами (то есть,
   например, при нажатии А изменялась на B, а B -- на A), и на вход роторам
   подавался измененный сигнал.

3. Каждый ротор -- шестерня, реализующая замену. Каждой букве алфавита ставится
   в соответствие другая буква этого же алфавита случайным образом. В
   лабораторной ротор реализован с помощью списка, описывающего, как перемешаны
   буквы в выходном алфавите, и целого числа, описывающего текущую позицию
   ротора. Зачем позиция? Дело в том, что роторы вращаются (см. пункт 6).

4. Рефлектор (англ. reflect -- отражать) попарно соединяет буквы одного
   алфавита. То есть весь алфавит делится на пары (поэтому в алфавите должно
   быть четное число букв), и при поступлении на вход буквы на выход подается
   ее "напарник" (например, если алфавит `abcd`, и есть пары `ad` и `bc`, то при
   входе `a` возращается `d`, при `d` -- `a`, при `b` -- `c`, при `c` -- `b`).
   Это свойство обеспечивает возможность использовать одну и ту же машину, как
   для шифрования, так и для расшифровки, необходимо только начинать оба
   действия при одних и тех же положениях роторов.

5. Как все это соединено? Три ротора соединены последовательно, на вход второго
   ротора подается выход первого, на вход третьего -- выход второго, рефлектору
   подается выход третьего рефлектора. Далее следует обратный ход, на нем
   рефлекторы работают наоборот, буква ищется в выходном алфавите, а
   возвращается буква из входного. Также буква через роторы проходит в обратном
   порядке: выход рефлектора подается третьему ротору, выход третьего --
   второму, выход второго -- первому. После такого "прогона" одной буквы роторы
   вращаются.

6. Первый ротор вращается после полного прохода каждой буквы, второй -- после
   того, как первый ротор сделает полный круг, вернувшись в начальную позицию,
   третий -- после того, как второй сделает полный круг (аналогично часам).

7. Готово. Для того, чтобы расшифровать сообщение, надо устновить роторы в те
   положения, при которых начиналось шифрование.

Подробно (или просто почитать и посмотреть):

[Картинки + код](https://medium.com/analytics-vidhya/how-to-build-an-enigma-machine-virtualisation-in-python-b5476a1fd922)

[Описание на русском](http://mediaknowledge.ru/ef0727594332a76f.html#.D0.9A.D0.BE.D0.BC.D0.BC.D1.83.D1.82.D0.B0.D1.86.D0.B8.D0.BE.D0.BD.D0.BD.D0.B0.D1.8F_.D0.BF.D0.B0.D0.BD.D0.B5.D0.BB.D1.8C)

[Листки с настройками Энигмы](https://ogn-slon.livejournal.com/293415.html)

[Еще описание на русском](https://habr.com/en/post/534066/)

[Красиво и полезно](https://www.youtube.com/watch?v=ybkkiGtJmkM) (by @hamzreg)