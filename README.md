# Log Analyzer

A script to process log files and generate reports.

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install tabulate
   

Basic usage:

python main.py --file example1.log --report average

python -m log_analyzer.main --file file1.log file2.log --report average

Filter by date:

python -m log_analyzer.main --file file.log --report average --date 2025-06-22

Run tests with:

pytest

Добавление новых отчетов:

1. Создайте новую функцию в reports.py, которая принимает журналы и возвращает данные отчета
2. Добавьте имя отчета к параметрам argparse в main.py
3. Добавьте обработку для нового отчета в основную функцию


### Особенности реализации:

1. **Модульная архитектура**:
   - Основная логика разделена на отдельные модули
   - Легко добавлять новые типы отчетов

2. **Обработка ошибок**:
   - Корректная обработка ошибок чтения файлов и парсинга JSON
   - Проверка формата даты

3. **Гибкость**:
   - Поддержка нескольких входных файлов
   - Фильтрация по дате
   - Возможность легко расширить функционал

4. **Тестирование**:
   - Покрытие основных функций тестами
   - Использование pytest и фикстур

### Пример вывода скрипта:

| Endpoint | Request Count | Average Response Time |

| /api/context/ | 15 | 0.038 |

| /api/homeworks/ | 42 | 0.142 |

| /api/specializations/| 6 | 0.032 |