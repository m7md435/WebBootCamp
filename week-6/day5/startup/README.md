# Startup Platform - URL Architecture Challenge ✅


## 📋 Requirements Met

### ✅ Requirement 1: App-Level URLs with Namespaces
Each app has its own `urls.py` file with proper namespacing:

| App | Namespace | Purpose |
|---|---|---|
| `users/` | `users` | User authentication & profiles |
| `courses/` | `courses` | Course browsing & management |
| `payments/` | `payments` | Payment processing & receipts |
| `dashboard/` | `dashboard` | User dashboard & reports |



---

### ✅ Requirement 2: Dynamic Routes
Implemented dynamic URL parameters across all apps:

```
/users/profile/<username>/              # Dynamic username
/courses/detail/<slug>/                 # Dynamic course slug
/courses/category/<category>/           # Dynamic category filter
/payments/receipt/<order_id>/           # Dynamic order identifier
/dashboard/reports/<report_type>/       # Dynamic report type
```

**Evidence:** Each route uses Django's path converters:
- `<slug:slug>` - for course slugs
- `<str:username>` - for string parameters
- `<str:category>` - for category filtering
- `<str:order_id>` - for order numbers
- `<str:report_type>` - for report types

---

### ✅ Requirement 3: Class-Based Views (CBV) - BONUS
Implemented multiple class-based views with `.as_view()` method:

| App | CBV | Route |
|---|---|---|
| users | `UserProfileView` | `/users/profile-cbv/<username>/` |
| courses | `CourseListView` | `/courses/` |
| payments | `CheckoutView` | `/payments/checkout/` |
| dashboard | `DashboardView` | `/dashboard/` |


---



