# Log Analyzer

Скрипт для обработки лог-файлов и создания отчетов.

## Installation

1. склонировать репозиторий
2. установить зависимости
   ```bash
   pip install tabulate
   

## Запуск скрипта:

python main.py --file example1.log --report average

### Фильтр по дате:

python -m main --file example1.log --report average --date 2025-06-22

## Запуск тестов:

pytest

### Особенности реализации:

1. **Модульная архитектура**:

2. **Обработка ошибок**:

3. **Гибкость**:
   - Поддержка нескольких входных файлов
   - Фильтрация по дате

4. **Тестирование**:
   - Покрытие основных функций тестами
   - Использование pytest

### Пример вывода скрипта:

| Endpoint      | Request Count | Average Response Time |

| /api/context/ | 15            | 0.038                 |

