@echo off
chcp 65001 >nul
title LinguaView 英语学习网站 - 一键启动

echo ============================================
echo.
echo   LinguaView 英语学习网站
echo   一键启动脚本
echo.
echo ============================================
echo.

cd /d "%~dp0"

REM 尝试多种方式启动HTTP服务器
where python >nul 2>nul
if %errorlevel%==0 (
    echo [正在使用 Python 启动服务器...]
    echo.
    echo ✅ 服务器已启动！
    echo    访问地址: http://localhost:8090
    echo.
    echo    首页: http://localhost:8090/index.html
    echo    目录: http://localhost:8090/catalog.html
    echo    学习: http://localhost:8090/learn.html
    echo    管理: http://localhost:8090/admin.html
    echo.
    echo    按 Ctrl+C 停止服务器
    echo ============================================
    echo.
    python -m http.server 8090
    goto end
)

where node >nul 2>nul
if %errorlevel%==0 (
    echo [正在使用 Node.js 启动服务器...]
    echo.
    echo ✅ 服务器已启动！
    echo    访问地址: http://localhost:8090
    echo.
    echo    首页: http://localhost:8090/index.html
    echo    目录: http://localhost:8090/catalog.html
    echo    学习: http://localhost:8090/learn.html
    echo    管理: http://localhost:8090/admin.html
    echo.
    echo    按 Ctrl+C 停止服务器
    echo ============================================
    echo.
    npx serve . -l 8090
    goto end
)

where npx >nul 2>nul
if %errorlevel%==0 (
    echo [正在使用 npx 启动服务器...]
    echo.
    echo ✅ 服务器已启动！
    echo    访问地址: http://localhost:8090
    echo.
    echo    首页: http://localhost:8090/index.html
    echo    目录: http://localhost:8090/catalog.html
    echo    学习: http://localhost:8090/learn.html
    echo    管理: http://localhost:8090/admin.html
    echo.
    echo    按 Ctrl+C 停止服务器
    echo ============================================
    echo.
    npx serve . -l 8090
    goto end
)

REM 如果没有检测到服务器软件
echo ============================================
echo.
echo   ⚠️  未检测到 Python 或 Node.js
echo.
echo   请先安装以下任一程序：
echo.
echo   Python（推荐）:
echo   1. 访问 https://www.python.org/downloads/
echo   2. 下载并安装 Python 3
echo   3. 勾选 "Add Python to PATH"
echo   4. 重新运行此脚本
echo.
echo   或直接使用（无需服务器）：
echo.
echo   双击以下文件即可使用：
echo   📄 index.html  - 首页
echo   📄 catalog.html - 学习目录
echo   📄 learn.html  - 精听学习
echo   📄 admin.html  - 管理后台
echo.
echo   注意：视频播放和翻译功能
echo   可能需要服务器支持
echo.
echo ============================================
echo.
pause

:end
