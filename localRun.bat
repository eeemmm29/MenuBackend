@echo off
SET CONTAINER_NAME=menu-backend
SET IMAGE_NAME=menu-backend
SET HOST_PORT=8000
SET CONTAINER_PORT=8000

REM Stop any running containers with the name 'menu-backend'
docker ps -q -f name=%CONTAINER_NAME% >nul 2>nul
IF NOT ERRORLEVEL 1 (
    echo Stopping the running '%CONTAINER_NAME%' container...
    docker stop %CONTAINER_NAME% >nul
    echo Removing the stopped '%CONTAINER_NAME%' container...
    docker rm %CONTAINER_NAME% >nul
) ELSE (
    echo No running container named '%CONTAINER_NAME%' found.
)

REM Remove any previous images with the name 'menu-backend'
docker images -q %IMAGE_NAME% >nul 2>nul
IF NOT ERRORLEVEL 1 (
    echo Removing the previous '%IMAGE_NAME%' Docker image...
    docker rmi %IMAGE_NAME% >nul
) ELSE (
    echo No image named '%IMAGE_NAME%' found.
)

REM Ensure .env file exists (or prompt user) - Assuming .env is managed manually for this project
REM If you have a template like .env.example, you could add:
REM IF NOT EXIST .env (
REM     echo .env file not found. Please create it from .env.example or manually.
REM     pause
REM     exit /b 1
REM )

echo Building the Docker image '%IMAGE_NAME%'...
docker build --target=development -t %IMAGE_NAME% .
IF ERRORLEVEL 1 (
    echo Docker build failed. Exiting.
    pause
    exit /b 1
)

echo Docker image built successfully.

echo Running the Docker container '%CONTAINER_NAME%'...
REM Runs in detached mode (-d), maps host port to container port (-p),
REM mounts the current directory to /app inside the container (-v),
REM uses the .env file for environment variables (--env-file),
REM and names the container (--name).
docker run --name %CONTAINER_NAME% --env-file .env -p %HOST_PORT%:%CONTAINER_PORT% -d -v "%CD%":/app %IMAGE_NAME%
IF ERRORLEVEL 1 (
    echo Failed to run the Docker container. Exiting.
    pause
    exit /b 1
)

echo Container '%CONTAINER_NAME%' is running.

echo Opening http://localhost:%HOST_PORT% in the browser...
start http://localhost:%HOST_PORT%

echo Script finished.