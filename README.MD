### Тестовое окружение
_Операционная система:_ Ubuntu 20.04

_Программное окружение:_ Python 3.8.5 установленый в pyenv 1.2.15-73

#### Установка зависимостей
Установите все необходимые зависимости используя команду:
```bash
pip install -r requirements.txt
```

#### Запуск тестов
Название тестов выбрано так, чтобы легко можно было их запускать через pytest -k
Для запуска тестов необхоимо перейти в корневой каталог проекта и запустить команду
``` bash
pytest
```

#### Генерация и просмотр отчетов
Генерация отчетов происходит автоматически.
Для просмотра отчетов необходимо установить docker-composer
```bash
docker-compose up -d allure
```

После этого результаты можно просмотреть в браузере.

#### Примечания

Файл с отчетом об исследовательском тестирование в корне репозитория: _Баг-репорт.docx_

Нужно нормально написать автотесты на нечеткий поиск и разделить на смоке и приемочное.
 
В задании так и не увидел границ, а сообщениям от сервера лучше не доверять (Например, на ограничение в 30 символов).
