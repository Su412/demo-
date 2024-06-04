from pickle import TRUE


{
    
   
        "version": "0.2.0",
        "configurations": [
            {
                "type": "node",
                "request": "launch",
                "name": "Launch Program",
                "skipFiles": [
                    "<node_internals>/**"
                ],
                "program": "${workspaceFolder}/api/index.js"
            },
            {
                "name": "Python: Flask",
                "type": "python",
                "request": "launch",
                "program": "${workspaceFolder}/app.py",
                "env": {
                    "FLASK_APP": "app.py",
                    "FLASK_ENV": "development"
                },
                "args": [
                    "run",
                    "--no-debugger",
                    "--no-reload"
                ],
                "jinja": TRUE
            }
        ]
    }
    