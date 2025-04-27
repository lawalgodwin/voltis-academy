# GraphQL Operations: Queries and Mutations

# ---
# Queries

```graphql
# 1. Users

# Fetch all users
query {
  users {
    userId
    firstName
    lastName
    email
    role
  }
}
```

```graphql
# Fetch a single user by ID
query GetUser($userId: UUID!) {
  user(userId: $userId) {
    userId
    firstName
    lastName
    email
    role
    settings {
      language
      timezone
      dateFormat
      notificationPreferences
    }
  }
}
```

# ---
# Courses

```graphql
# Fetch all courses
query {
  courses {
    courseId
    title
    description
    category
    duration
    createdAt
    updatedAt
    instructor {
      userId
      firstName
      lastName
    }
  }
}
```

```graphql
# Fetch a single course by ID
query GetCourse($courseId: UUID!) {
  course(courseId: $courseId) {
    courseId
    title
    description
    category
    duration
    instructor {
      userId
      firstName
    }
  }
}
```

# ---
# Enrollments

```graphql
# Fetch all enrollments
query {
  enrollments {
    enrollmentId
    enrollmentDate
    completionStatus
    student {
      userId
      firstName
      lastName
    }
    course {
      courseId
      title
    }
  }
}
```

```graphql
# Fetch enrollments for a specific course
query CourseEnrollments($courseId: UUID!) {
  enrollmentsByCourse(courseId: $courseId) {
    enrollmentId
    student {
      userId
      firstName
    }
    completionStatus
  }
}
```

# ---
# Appointments

```graphql
# Fetch all appointments
query {
  appointments {
    appointmentId
    appointmentDate
    status
    student {
      userId
      firstName
    }
    instructor {
      userId
      firstName
    }
  }
}
```

```graphql
# Fetch a single appointment by ID
query GetAppointment($appointmentId: UUID!) {
  appointment(appointmentId: $appointmentId) {
    appointmentId
    appointmentDate
    status
  }
}
```

# ---
# Settings

```graphql
# Fetch current user's settings
query {
  mySettings {
    settingsId
    language
    timezone
    dateFormat
    notificationPreferences
  }
}
```

# ---
# Mutations

```graphql
# 1. Authentication

# Register a new user
mutation Register(
  $email: String!
  $password: String!
  $firstName: String!
  $lastName: String!
  $role: String!
) {
  register(
    email: $email
    password: $password
    firstName: $firstName
    lastName: $lastName
    role: $role
  ) {
    user {
      userId
      email
      firstName
      lastName
      role
    }
  }
}
```

```graphql
# Sign in (JWT)
mutation SignIn($email: String!, $password: String!) {
  signIn(email: $email, password: $password) {
    token
    refreshToken
  }
}
```

```graphql
# Refresh token
mutation RefreshToken($refreshToken: String!) {
  refreshToken(refreshToken: $refreshToken) {
    token
    refreshToken
  }
}
```

```graphql
# Logout / Revoke refresh token
mutation LogOut($refreshToken: String!) {
  logOut(refreshToken: $refreshToken) {
    revoked
  }
}
```

# ---
# Course Operations

```graphql
# Create a course
mutation CreateCourse(
  $title: String!
  $description: String!
  $instructorId: UUID!
  $category: String!
  $duration: String!
) {
  createCourse(
    title: $title
    description: $description
    instructorId: $instructorId
    category: $category
    duration: $duration
  ) {
    course {
      courseId
      title
    }
  }
}
```

```graphql
# Update a course
mutation UpdateCourse(
  $courseId: UUID!
  $title: String
  $description: String
  $category: String
  $duration: String
) {
  updateCourse(
    courseId: $courseId
    title: $title
    description: $description
    category: $category
    duration: $duration
  ) {
    course {
      courseId
      title
      updatedAt
    }
  }
}
```

# ---
# Enrollment

```graphql
# Enroll a student in a course
mutation EnrollForCourse($courseId: UUID!, $studentId: UUID!) {
  enrollForCourse(courseId: $courseId, studentId: $studentId) {
    enrollment {
      enrollmentId
      completionStatus
    }
  }
}
```

# ---
# Appointment

```graphql
# Book a new appointment
mutation BookAppointment(
  $studentId: UUID!
  $instructorId: UUID!
  $appointmentDate: DateTime!
) {
  bookAppointment(
    studentId: $studentId
    instructorId: $instructorId
    appointmentDate: $appointmentDate
  ) {
    appointment {
      appointmentId
      status
    }
  }
}
```

```graphql
# Update an appointment's status
mutation UpdateAppointment(
  $appointmentId: UUID!
  $status: String!
) {
  updateAppointment(appointmentId: $appointmentId, status: $status) {
    appointment {
      appointmentId
      status
      updatedAt
    }
  }
}
```

# ---
# Settings

```graphql
# Create or update settings
mutation CreateOrUpdateSettings(
  $userId: UUID!
  $language: String!
  $timezone: String!
  $dateFormat: String!
  $notificationPreferences: JSON!
) {
  createOrUpdateSettings(
    userId: $userId
    language: $language
    timezone: $timezone
    dateFormat: $dateFormat
    notificationPreferences: $notificationPreferences
  ) {
    settings {
      settingsId
      language
      timezone
      dateFormat
      notificationPreferences
    }
  }
}
```

```graphql
# Update just notification preferences
mutation UpdateNotificationPreferences($notificationPreferences: JSON!) {
  updateNotificationPreferences(notificationPreferences: $notificationPreferences) {
    settings {
      settingsId
      notificationPreferences
    }
  }
}
```
