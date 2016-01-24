
python tools\tool.py

cd gyp
..\tools\gyp\gyp.bat test-client.gyp --depth=.. -Gmsvs_version=2013 -fmsvs --generator-output=../out

pause
