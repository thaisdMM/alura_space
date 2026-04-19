# 🌌 Alura Space

Alura Space is a **Django-based web application** developed as part of a learning path focused on building web projects with Django.
The project evolves progressively through multiple branches, each one applying new concepts on top of the same codebase.

The application represents a **space photography gallery**, where images are displayed with contextual information and managed through Django features introduced step by step.

> 🎯 Focus: Django backend fundamentals and intermediate concepts
> 🎨 Note: The HTML/CSS base was provided by the courses; the emphasis is on Django development.

---

## ✨ Project Overview

Alura Space is a gallery-style application that displays space images (nebulae, stars, galaxies, planets), showing details such as titles and descriptions.
As the project evolves, new backend features are added, such as database persistence, administrative management, media handling, and search functionality.

---

## 🧩 Project Structure & Learning Path

The repository is organized by **branches**, each representing a different stage of learning within the same project.

---

## 🌱 `main` — Django Templates & Best Practices

This branch establishes the **foundation of the project**.

**Key concepts applied:**

- Django project and app structure
- Views and URL configuration
- Template rendering
- Static files configuration
- Template inheritance, partials, and DRY principles
- Basic environment configuration

**Purpose:**
Create a clean, well-structured Django project that serves as the base for future backend features.

---

## 🚀 `persistencia-dados-e-admin` — Data Persistence & Django Admin

This branch builds upon the base project and introduces **core backend functionality**.

**Key concepts applied:**

- Data persistence using Django ORM
- Model creation and database migrations
- SQLite3 database integration
- Django Admin configuration and customization
- Content management through the admin interface
- Media file handling (image uploads and display)
- Data filtering, ordering, and basic search functionality

**Purpose:**
Transform the project into a dynamic application backed by a database, enabling content management and real-world data handling.

---

## 🔐 `autenticacao-formularios-alertas` — Forms, Authentication & Alerts

This branch extends the project by introducing **user interaction and authentication features** using Django’s built-in tools.

**Key concepts applied:**

- Django Forms and form rendering
- Form data validation and error handling
- CSRF protection
- User authentication (login, logout, registration)
- Dynamic alert and feedback messages
- Association between users and application data
- Use of partials to reduce template duplication

**Purpose:**
Add controlled user interaction to the application, enabling authentication workflows, validated form submissions, and dynamic user feedback while maintaining clean template organization.

---

## 🔧 `refactor/project-structure` — Template Architecture & Code Quality _(Personal Initiative)_

After completing the course branches, **I decided to refactor the project** to improve code organization, maintainability, and professional standards - applying best practices and clean code principles.

**Key improvements:**

- **Template Architecture Redesign**
  Created hierarchical template inheritance (`base.html` → `base_galeria.html`/`base_auth.html` → pages) with strategic blocks for flexibility

- **Code Deduplication (DRY Principle)**
  Eliminated ~70% of duplicate HTML by consolidating authentication and gallery templates into reusable components (`form_auth.html`, `gallery_list.html`, `_cards.html`, `_header.html`)

- **Separation of Concerns**
  Extracted and reorganized partials with single clear responsibilities, fixing structural HTML issues (unclosed tags across files)

- **Enhanced Search Functionality**
  Improved search to filter by both photo name and category, added clickable category tags for intuitive filtering

- **Dynamic Content**
  Replaced hardcoded values with database-driven content (photo categories, page titles)

**Technical decisions:**
Isolated Bootstrap to authentication pages only, preventing CSS conflicts. Applied Conventional Commits standard for clear change history.

**Result:**
Transformed a functional learning project into a maintainable, production-ready codebase following Django and software engineering best practices.

---

## 🛠️ Technologies Used

- Python
- Django
- SQLite3
- HTML & CSS (provided base)

---

## 📌 Notes

- This project is part of a **progressive learning series**, not a production-ready application.
- Branches are intentionally kept independent to preserve each learning stage.
- To explore a specific learning stage, switch to the corresponding branch.
- Future branches continue expanding the same project with additional Django features.

---

📷 _Alura Space — exploring the universe through Django._
