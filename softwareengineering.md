# **TasteTracker – Project Documentation**  
*(For your Practical Project & Folio)*

---

# **1. Requirements Documentation**

## **1.1 Functional Requirements**
TasteTracker must allow users to:

### **User Accounts**
- Register a new account securely  
- Log in using a hashed password  
- Log out safely  
- Set or update a nickname  

### **Review Features**
- Logged‑in users can:
  - Add a restaurant review  
  - Edit their own reviews  
  - Delete their own reviews  
- Reviews must include:
  - Restaurant Name  
  - Cuisine Type  
  - Review Date  
  - Rating (0–10)  
  - Review Text  

### **Viewing & Searching**
- All users (including guests) can view all reviews  
- Users can:
  - Search reviews by text  
  - Filter by rating  
  - Filter by username  
  - Sort reviews (e.g., highest rated)  
- Live search updates results without reloading the page  

### **PWA Requirements**
- App must install as a PWA  
- Must work offline using a service worker  
- Must include a manifest.json and icons  

---

## **1.2 Non‑Functional Requirements**
- Works on desktop, tablet, and mobile  
- Clean, simple, intuitive UI  
- Secure password hashing  
- SQL database with safe storage  
- Fast load times  
- No horizontal scrolling  
- Uses Flask + Jinja2 templates  
- Uses GitHub for version control and Agile workflow  

---

## **1.3 Constraints**
- Must use:
  - Python Flask  
  - Jinja2  
  - SQLite  
  - HTML, CSS, JavaScript  
  - GitHub for version control  
- Must follow secure coding practices  
- Must block unauthorized access to review editing/deleting  

---

## **1.4 Acceptance Criteria**
- Users can register, log in, add/edit/delete reviews  
- Database stores all review data  
- Search and filtering work correctly  
- PWA installs and works offline  
- Code is modular and documented  
- GitHub Project Board shows Agile workflow  
- UI is responsive and user‑friendly  

---

# **2. IPO Charts**

## **2.1 Login System**
| Input | Process | Output |
|-------|---------|--------|
| Username, Password | Check DB → verify password hash → create session | User logged in or error message |

## **2.2 Create Review**
| Input | Process | Output |
|-------|---------|--------|
| Title, Content, Rating | Validate → save to DB → link to user | Review saved |

## **2.3 Edit Review**
| Input | Process | Output |
|-------|---------|--------|
| Updated title/content/rating | Check ownership → update DB | Review updated |

## **2.4 Search Reviews**
| Input | Process | Output |
|-------|---------|--------|
| Search text, rating, username | Filter DB → return JSON | Updated review list |

---

# **3. Storyboard (Page Layouts)**

### **Home Page**
- Navigation: Home, Login, Signup, Dashboard  
- Live user count  
- Welcome message  

### **Signup Page**
- Username field  
- Password field  
- Submit button  

### **Login Page**
- Username  
- Password  
- Login button  

### **Dashboard**
- Random review  
- Buttons: Make Review, Lists, Logout  

### **Make Review**
- Title  
- Rating  
- Content  
- Submit  

### **Lists Page**
- Your Reviews  
- Search + Filter  
- Live‑updating All Reviews  
- Edit buttons for your reviews  

### **Edit Review Page**
- Pre‑filled form  
- Save changes  

---

# **4. Data Dictionary**

## **Users Table**
| Field | Type | Description |
|-------|------|-------------|
| id | Integer (PK) | Unique user ID |
| username | Text | Login name |
| password | Text | Hashed password |
| nickname | Text | Display name |

## **Reviews Table**
| Field | Type | Description |
|-------|------|-------------|
| id | Integer (PK) | Review ID |
| username | Text | Author (nickname or username) |
| title | Text | Restaurant name |
| content | Text | Review text |
| rating | Integer | Rating 0–10 |

---

# **5. Pseudocode / Algorithms**

## **5.1 Secure Login Algorithm**
```
FUNCTION login():
    IF request is POST:
        username ← form input
        password ← form input

        user ← find user in database by username

        IF user exists AND password hash matches:
            store user_id in session
            store username in session
            REDIRECT to dashboard
        ELSE:
            SHOW "Invalid username or password"
    ELSE:
        SHOW login page
```

## **5.2 Create Review Algorithm**
```
FUNCTION make_review():
    IF user not logged in:
        REDIRECT to login

    IF request is POST:
        title ← form input
        content ← form input
        rating ← form input

        review ← new Review(user, title, content, rating)
        save review to database

        REDIRECT to dashboard
    ELSE:
        SHOW review form
```

## **5.3 Edit Review Algorithm**
```
FUNCTION edit_review(review_id):
    IF user not logged in:
        REDIRECT to login

    review ← find review by ID
    user ← current logged-in user

    IF review.username != user.nickname:
        SHOW "Unauthorized"

    IF request is POST:
        update review fields
        save changes
        REDIRECT to lists
    ELSE:
        SHOW edit form with existing data
```

## **5.4 Live Search Algorithm**
```
FUNCTION api_reviews():
    read search, rating, user from URL

    query ← all reviews

    IF search provided:
        filter title OR content contains search

    IF rating provided:
        filter rating equals rating

    IF user provided:
        filter username contains user

    RETURN results as JSON
```

---

# **6. Agile Workflow (What to Write in Your Diary)**

### **Daily/Sprint Reflection Examples**
- What you planned  
- What you completed  
- Problems you hit  
- How you solved them  
- What you will do next  

### **Example Diary Entry**
```
Day 4:
Planned: Implement live search API.
Completed: Built /api/reviews route, added JS fetch logic.
Issue: JSON wasn't updating because of wrong element ID.
Fix: Corrected DOM selector and added event listeners.
Next: Add edit review functionality.
```

---

# **7. GitHub Project Board Requirements**

Your board should include:

### Columns:
- Backlog  
- Ready  
- In Progress  
- In Review  
- Done  

### Issues Examples:
- Create DB schema  
- Build signup/login  
- Add review CRUD  
- Implement search/filter  
- Add PWA service worker  
- Add edit review page  
- Fix horizontal scrolling  

---

# **8. UI & UX Notes**
- No horizontal scrolling  
- Clean centered layout  
- Responsive CSS  
- Buttons easy to tap on mobile  
- Live search feels modern and fast  

