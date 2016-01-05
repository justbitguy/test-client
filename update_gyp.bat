:: 当按下面的格式写的时候
:: tools\gyp\gyp.bat gyp\test-client.gyp --depth=. -Gmsvs_version=2013 -fmsvs --generator-output=out
:: 会生成比较繁琐的目录结构: out\gyp

python tools\tool.py

cd gyp
..\tools\gyp\gyp.bat test-client.gyp --depth=.. -Gmsvs_version=2013 -fmsvs --generator-output=../out

pause
