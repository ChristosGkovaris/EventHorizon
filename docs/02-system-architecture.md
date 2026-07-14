# System Architecture

## 1. Architecture Goal

The system should receive log events from simulated services, validate them,
store them in the correct systems, and expose them through a web interface.

Users should be able to search logs, filter them by service and severity,
and investigate related events.

The initial architecture should remain simple enough to understand and test,
while allowing later improvements in scalability and deployment.

---

## 2. Main Components

- **React frontend** — Displays logs, filters, search results, dashboards, and incident details.
- **Flask backend API** — Receives requests from the frontend and log generator, validates the data, and communicates with PostgreSQL and OpenSearch.
- **Log generator** — Creates realistic fake logs so the system can be developed and tested without needing real servers.
- **PostgreSQL database** — Stores the application's structured data, such as users, saved searches, settings, and other metadata.
- **OpenSearch** — Indexes and stores log data, allowing engineers to perform fast full-text searches, filtering, and log analysis.
- **Docker Compose** — Runs and connects all project services together, allowing the entire application to start with a single command.

---

## 3. Data Flow



---

## 4. Responsibilities of Each Component



---

## 5. Technology Choices



---

## 6. Initial Architecture Diagram

Log Generator
      |
      | POST /api/logs
      v
Flask Backend API
      |
      | index raw logs
      v
OpenSearch

React Frontend
      |
      | GET /api/logs/search
      v
Flask Backend API
      |
      +------> OpenSearch
      |
      +------> PostgreSQL

---

## 7. Open Questions



---