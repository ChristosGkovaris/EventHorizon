# EVENTHORIZON-OBSERVATORY-PLATFORM

EventHorizon is a **full-stack observability platform under active development**, designed for centralized log collection, querying, filtering, and analysis. The project currently provides a **Flask-based REST API** with modular routing, service-layer separation, health monitoring, and structured log retrieval.

---

## TABLE OF CONTENTS

1. [Overview](#overview)
2. [Tech Stack](#tech-stack)
3. [Features](#features)
4. [Architecture](#architecture)
5. [Project Structure](#project-structure)
6. [API Endpoints](#api-endpoints)
7. [Log Data](#log-data)
8. [Installation](#installation)
9. [Usage](#usage)
10. [Development Roadmap](#development-roadmap)
11. [License](#license)
12. [Contact](#contact)

---

## OVERVIEW

EventHorizon is an observability platform designed to provide a centralized environment for managing and inspecting application logs.

The project is being developed incrementally, beginning with the backend infrastructure required to expose, organize, and query log data through a REST API.

The current implementation focuses on:

* Flask application initialization
* REST API endpoint design
* Modular route organization using Flask Blueprints
* Separation of routing and log-related logic
* Structured JSON log representation
* Log retrieval
* Severity-based log filtering
* Service identification
* Application health monitoring
* Initial architecture and project documentation

The long-term architecture is designed to evolve into a complete observability system with a web frontend, persistent log storage, search infrastructure, containerization, authentication, testing, and automated deployment workflows.

---

## TECH STACK

### Currently Used

* **Language:** Python
* **Backend:** Flask
* **API:** REST
* **Data Format:** JSON
* **Architecture:** Modular Flask application, Blueprints, Service Layer
* **Version Control:** Git, GitHub
* **Documentation:** Markdown

### Planned

* **Frontend:** React, JavaScript / TypeScript
* **Database:** PostgreSQL
* **Search & Indexing:** Elasticsearch / OpenSearch
* **Containerization:** Docker, Docker Compose
* **Authentication:** User authentication and authorization
* **Testing:** Automated backend and integration testing
* **CI/CD:** GitHub Actions
* **Deployment:** OpenShift

---

## FEATURES

### REST API

The backend exposes REST endpoints for accessing EventHorizon functionality and returns structured JSON responses.

### Health Monitoring

A dedicated health endpoint provides information about the current state of the backend service.

Example response:

```json
{
  "service": "EventHorizon",
  "status": "healthy"
}
```

### Log Retrieval

The logs endpoint provides access to structured application log entries.

Each log can contain information such as:

* Log ID
* Service
* Severity
* Message

### Severity Filtering

Log results can be filtered through HTTP query parameters.

Example:

```text
/logs?severity=ERROR
```

The backend evaluates the requested severity and returns only matching log entries.

### Service Identification

Log entries contain service information, allowing logs to be associated with the application component or service that generated them.

Examples include:

```text
auth-service
payment-service
database-service
```

### Modular Routing

Flask Blueprints separate endpoint definitions from the main application configuration.

This prevents the central Flask application from becoming responsible for every individual route.

### Service-Layer Separation

Log-related data and logic are separated from HTTP route handling.

This provides a clearer boundary between:

```text
HTTP Request
      ↓
Route / Blueprint
      ↓
Service Logic
      ↓
Log Data
      ↓
JSON Response
```

### Architecture Documentation

The repository contains project documentation describing:

* Project vision
* Architecture goals
* Main system components
* Initial architecture design

---

## ARCHITECTURE

EventHorizon follows a modular architecture intended to separate HTTP communication, application logic, data management, and future infrastructure components.

### Flask Application

The Flask application acts as the backend entry point.

It initializes the application and registers the required Blueprints.

API routing is organized under a common API prefix rather than embedding the prefix independently into every endpoint.

### Route Layer

Routes are responsible for:

* Receiving HTTP requests
* Reading request parameters
* Calling the appropriate application logic
* Returning HTTP/JSON responses

Blueprints are used to organize related endpoints into independent modules.

### Service Layer

Application logic is separated from route definitions where appropriate.

The log service is responsible for log-related operations and prevents the HTTP layer from directly owning all log data and processing logic.

Conceptually:

```text
CLIENT
   │
   │ HTTP Request
   ▼
FLASK APPLICATION
   │
   ▼
BLUEPRINT / ROUTE
   │
   ▼
SERVICE LAYER
   │
   ▼
LOG DATA
   │
   ▼
JSON RESPONSE
```

### Future Architecture

The current backend forms the foundation for a larger observability architecture:

```text
Applications / Log Generator
            │
            ▼
      EventHorizon API
            │
      ┌─────┴─────┐
      ▼           ▼
 PostgreSQL    OpenSearch
      │           │
      └─────┬─────┘
            ▼
      Flask Backend
            │
            ▼
       React Frontend
```

PostgreSQL, OpenSearch, the React frontend, and the log generator integration represent planned stages of the project rather than completed functionality.

---

## PROJECT STRUCTURE

```text
EventHorizon/
│
├── .github/
│   └── workflows/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   │
│   └── routes/
│       ├── __init__.py
│       ├── health.py
│       └── logs.py
│
├── docs/
│
├── frontend/
│
├── infrastructure/
│
├── log-generator/
│
├── tests/
│
├── .gitignore
├── LICENSE
├── docker-compose.yml
├── Makefile
└── README.md
```

The repository is organized around the major components required by the final EventHorizon platform.

Some directories currently provide the structural foundation for functionality planned in later development stages.

---

## API ENDPOINTS

### Health Endpoint

```http
GET /api/health
```

Returns information about the current state of the EventHorizon backend.

Example:

```json
{
  "service": "EventHorizon",
  "status": "healthy"
}
```

### Logs Endpoint

```http
GET /api/logs
```

Returns the available log entries.

### Severity Filter

```http
GET /api/logs?severity=ERROR
```

Returns logs matching the requested severity.

Supported log severities currently include:

```text
INFO
WARNING
ERROR
```

The filtering process evaluates the `severity` query parameter against the severity associated with each available log.

---

## LOG DATA

The current backend uses structured log entries during the initial API-development stage.

Example:

```json
{
  "id": 1,
  "service": "auth-service",
  "severity": "INFO",
  "message": "User logged in successfully"
}
```

Current example services include:

* `auth-service`
* `payment-service`
* `database-service`

Example log messages represent events such as:

* Successful user authentication
* Payment request timeouts
* Database connection-pool warnings

This initial data model provides the foundation for later integration with persistent storage and generated or externally collected logs.

---

## INSTALLATION

1. Clone the repository:

```bash
git clone https://github.com/ChristosGkovaris/EventHorizon.git
cd EventHorizon
```

2. Navigate to the backend:

```bash
cd backend
```

3. Create a Python virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment.

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

6. Start the Flask backend:

```bash
python app.py
```

---

## USAGE

After starting the backend, API requests can be sent to the running Flask server.

### Check Backend Health

```http
GET /api/health
```

### Retrieve Logs

```http
GET /api/logs
```

### Retrieve ERROR Logs

```http
GET /api/logs?severity=ERROR
```

### Retrieve WARNING Logs

```http
GET /api/logs?severity=WARNING
```

### Retrieve INFO Logs

```http
GET /api/logs?severity=INFO
```

The API returns matching log entries as JSON responses.

---

## DEVELOPMENT ROADMAP

EventHorizon is under active development.

Planned development stages include:

* [x] Initialize repository structure
* [x] Create Flask backend
* [x] Implement backend health endpoint
* [x] Introduce Flask Blueprints
* [x] Implement logs API endpoint
* [x] Implement severity-based log filtering
* [x] Separate log-related logic into a service layer
* [x] Add service identification to log entries
* [x] Create initial architecture documentation
* [ ] Expand automated backend tests
* [ ] Implement log generator
* [ ] Integrate PostgreSQL persistence
* [ ] Integrate Elasticsearch / OpenSearch
* [ ] Implement React frontend
* [ ] Add authentication and authorization
* [ ] Complete Docker / Docker Compose environment
* [ ] Implement CI/CD pipeline
* [ ] Add production deployment configuration
* [ ] Deploy using OpenShift

---

## LICENSE

This project is licensed under the **MIT License**.

See the `LICENSE` file for the complete license terms.

---

## CONTACT

**Christos-Grigorios Gkovaris**
Computer Science and Engineering
University of Ioannina