@echo off
chcp 65001 >nul
title LinguaView 翻译服务

echo ========================================
echo   LinguaView 视频翻译服务启动器
echo ========================================
echo.

echo [1/4] 检查Python环境...
python --version
if %errorlevel% neq 0 (
    echo.
    echo 错误：未找到Python，请先安装Python 3.8+
    echo 下载地址：https://www.python.org/downloads/
    pause
    exit /b 1
)

echo.
echo [2/4] 安装依赖包...
pip install fastapi uvicorn requests

echo.
echo [3/4] 检查端口占用...
netstat -ano | findstr :8001
if %errorlevel% equ 0 (
    echo 端口 8001 被占用，尝试释放...
    for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8001') do (
        taskkill /F /PID %%a
        echo 已终止进程 PID: %%a
    )
    timeout /t 2 /nobreak >nul
)

echo.
echo [4/4] 启动后端服务...
echo.
echo 服务地址: http://localhost:8001
echo 健康检查: http://localhost:8001/api/health
echo.
echo 请保持此窗口打开，不要关闭！
echo 按 Ctrl+C 停止服务
echo.

cd /d "%~dp0api"
python transcribe.py

pause