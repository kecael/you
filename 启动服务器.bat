@echo off
chcp 65001 >nul
title LinguaView 英语学习网站

echo ============================================
echo   LinguaView 英语学习网站 - 启动器
echo ============================================
echo.

cd /d "%~dp0"

REM 检查 Python
where python >nul 2>nul
if %errorlevel%==0 (
    echo [1] 使用 Python 启动服务器...
    echo 服务器地址: http://localhost:8090
    echo.
    echo 按 Ctrl+C 停止服务器
    echo ============================================
    python -m http.server 8090
    goto end
)

REM 检查 Node.js
where node >nul 2>nul
if %errorlevel%==0 (
    echo [2] 使用 Node.js 启动服务器...
    echo 服务器地址: http://localhost:8090
    echo.
    echo 按 Ctrl+C 停止服务器
    echo ============================================
    npx serve . -l 8090
    goto end
)

REM 检查 npx
where npx >nul 2>nul
if %errorlevel%==0 (
    echo [3] 使用 npx 启动服务器...
    echo 服务器地址: http://localhost:8090
    echo.
    echo 按 Ctrl+C 停止服务器
    echo ============================================
    npx serve . -l 8090
    goto end
)

echo ============================================
echo   未检测到 Python 或 Node.js
echo   请先安装以下任一程序:
echo   
echo   Python: https://www.python.org/downloads/
echo   Node.js: https://nodejs.org/
echo ============================================
echo.
echo 或者直接双击打开 index.html 文件
echo.
pause

:end
