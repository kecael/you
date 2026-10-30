@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ============================================
echo    LinguaView 英语学习网站
echo    正在启动本地服务器...
echo ============================================
echo.
echo 服务器启动后，请在浏览器访问:
echo http://localhost:8090
echo.
echo 按 Ctrl+C 停止服务器
echo ============================================
echo.
python -m http.server 8090
pause
