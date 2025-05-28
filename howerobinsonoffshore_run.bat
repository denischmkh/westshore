@echo off
cd /d %~dp0

REM Активируем виртуальное окружение
call venv\Scripts\activate

REM Устанавливаем зависимости из requirements.txt
pip install -r req.txt

REM Запускаем скрипт 1
python modules\3_parse_table_howerobinsonoffshore.py