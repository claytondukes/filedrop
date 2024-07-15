# Post-Setup operation

```
cd /downloads/filedrop
d compose up
```

Then point the user to https://license.logzilla.net/upload (this is set up on our proxy ssl to redirect
license.logzilla.net/upload to this server)

After they upload, check the /downloads/filedrop/uploads directory




# Initial Setup

## Docker-based filedrop app

This is a simple Flask application for uploading and listing files. The application is containerized using Docker and can be easily deployed using Docker Compose.

### Features

- Upload files
- List uploaded files
- Download files

### Prerequisites

- Docker
- Docker Compose

### Project Structure

```
.
├── Dockerfile
├── LICENSE
├── README.md
├── app.py
├── docker-compose.yml
├── requirements.txt
├── templates
│   └── index.html
└── uploads
    └── file1.txt
```

### Setup and Running

1. **Clone the repository:**

    ```
    git clone https://github.com/claytondukes/filedrop.git
    cd filedrop
    ```

2. **Build and start the application using Docker Compose:**

    ```
    docker compose up --build
    ```

3. **Access the application:**

    Open your web browser and go to `http://localhost:8080`.

### File Upload

To upload a file, use the upload form provided on the main page of the application. The uploaded files will be saved in the `uploads` directory.

### File Listing

To list all uploaded files, navigate to the `/list` endpoint. The files will be displayed in a table format.

### Download Files

To download a file, navigate to `http://localhost:8080/uploads/<filename>`, replacing `<filename>` with the name of the file you want to download.

### Cleaning Up

To stop the application and remove the containers, run:

```
docker compose down
```

### Contributing

Feel free to open issues or submit pull requests if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
