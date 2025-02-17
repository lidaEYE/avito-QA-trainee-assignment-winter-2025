# Решение тестового задания для стажёра QA-направления (зимняя волна 2025)
Репозиторий содержит решение тестового задания для стажёров QA-направления в Avito Tech.

  Исходное задание можно посмотреть [тут](QA-trainee-assignment-winter-2025.md)

## Структура проекта
```
├── Task1 - папка 1 задания
│   ├── img                      - папка со скриншотами багов
│   └── BUGS_FROM_SCREENSHOT.md  - файл с описанием найденных багов
│
├── Task2 - папка 2 задания
│   ├── 
│   ├── TESTCASES.md             - выполненные тест кейсы
│   └── 
├── 
├── requirements.txt
└── README.md
```

### Задание 1. Поиск багов
Полное решение задания расположено в файле [BUGS_FROM_SCREENSHOT.md](Task1/BUGS_FROM_SCREENSHOT.md)

### Задание 2.1
* Тест-кейсы оформлены в файле [TESTCASES.md](Task2/TESTCASES.md)
* Баг-репорт оформлен в файле [BUGS.md](Task2/BUGS.md)
* Автоматизацию тест-кейсов пыталась выполнить в файле [test_avito.py](Task2/auto_tests/test_avito.py)....




### Инструкция   

1. Склонируйте к себе репозиторий, в котором хранится проект тестового задания, через выполнение команды в терминале  
    ```  
    git clone https://github.com/avito-tech/tech-internship.git
    ```  
    Или скачайте zip-архив по [ссылке](https://github.com/Herzenswearme/AvitoTech\_QA-trainee/archive/refs/heads/main.zip) и распакуйте его

2. Убедитесь, что на вашем компьютере установлен Python. В командной строке/терминале выполните команду  
    ```  
    python -v  
    ```    
Если он не установлен, то установите с официального [сайта Python](https://www.python.org/downloads/), выбрав подходящую версию для вашей операционной системы, и пройдите шаг сначала. В процессе установки обязательно поставьте галочку в чекбоксе "Add python.exe to PATH". 

1. Через командную строку/терминал перейдите в корневую директорию проекта, выполнив команду  
   ```  
   cd /здесь укажите путь до директории с проектом  
   ```
2. Установите необходимые зависимости из файла `requirements.txt`, выполнив команду    
   ```  
   pip install -r requirements.txt  
   ```  
   если она не выполняется, то попробуйте  
   ```  
   pip3 install -r requirements.txt  
   ```  
3. После выполнения предыдущего пункта установите необходимые бинарные файлы браузеров, выполнив команду  
   ```  
   playwright install  
   ```  
     
4. Наконец, запустите тесты, выполнив команду    
   ```  
   pytest -v  
   ```  