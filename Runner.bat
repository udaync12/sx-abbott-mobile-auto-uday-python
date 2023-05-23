set timestamp = %date:~7,2%%date:~4,2%%date:~10,4%_%time:~0,2%%time:~3,2%%time:~6,2%
pytest -v -s --html=.\Reports\%timestamp%_report.html --self-contained-html TestRunner.py