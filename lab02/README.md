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

TODO
