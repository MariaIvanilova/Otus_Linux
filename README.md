# Otus_Linux
## Работа с ОС Linux с помощью Python

### Цель:

Попрактиковаться в работе с процессами ОС Linux

### Описание:

Для выполнения задания нужно написать парсер системных процессов команды `ps aux` на языке Python с использованием 
стандартной библиотеки и модуля `subprocess`. Парсер должен вывести в стандартный вывод в качестве результата работы 
следующую информацию (все цифры и данные для примера):

```bash
Отчёт о состоянии системы:
Пользователи системы: 'root', 'user1', ...
Процессов запущено: 833

Пользовательских процессов:
root: 533
user1: 231
...

Всего памяти используется: 23.1%
Всего CPU используется: 33.2%
Больше всего памяти использует: (%имя процесса, первые 20 символов если оно длиннее)
Больше всего CPU использует: (%имя процесса, первые 20 символов если оно длиннее)
```

Так же этот отчёт должен быть сохранён в отдельный txt файл с названием текущей даты и времени проверки. 
Например, `10-12-2021-12:15-scan.txt`

### Критерии оценки:

Статус "Принято" ставится, если:

1. Скрипт выводит в стандартый поток вывода корректную статистику по запущенным процессам
2. Скрипт формирует txt файл, в котором сохранена статистика по запущенным процессам
3. Предоставлены скриншоты работы скрипта (терминала с информацией о процессах)
4. Задание выполнено и оформлено отдельным pull-request'ом
5. Соблюдается минимальный кодстайл для проекта
6. В pull-request отсутствуют лишние файлы не относящиеся к заданию
