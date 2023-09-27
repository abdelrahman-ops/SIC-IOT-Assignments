function validateEmail(email) {
    // Define a regular expression pattern for email validation
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
  
    // Test the input email against the pattern
    return emailPattern.test(email);
}

console.log(validateEmail("john.doe@example.com")); // true
console.log(validateEmail("invalid-email")); // false
console.log(validateEmail("another@example")); // false
  