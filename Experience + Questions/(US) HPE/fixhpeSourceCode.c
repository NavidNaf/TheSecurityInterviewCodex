/*
* Fixed version of hpeSourceCode.c
* Language: C
*/

#include <stdio.h>
#include <string.h>

#define USERNAME_SIZE 16

typedef struct {
   char username[USERNAME_SIZE];
   int is_admin;
} User;

// Function to process user login
int process_login(const char *input) {
   // Fix: initialize the full struct to zero.
   // This makes sure username is empty and is_admin starts as 0.
   User u = {0};

   // Fix: validate input length before copying it into username.
   // username can hold 15 visible characters plus the null terminator.
   if (strlen(input) >= sizeof(u.username)) {
       fprintf(stderr, "Error: username must be shorter than %zu characters.\n", sizeof(u.username));
       return 1;
   }

   // Fix: use snprintf instead of strcpy.
   // snprintf respects the destination buffer size and always null-terminates
   // as long as the buffer size is greater than 0.
   snprintf(u.username, sizeof(u.username), "%s", input);

   // Fix: is_admin cannot be changed by overflowing username anymore, because the copy above is bounded and oversized input is rejected.
   if (u.is_admin) {
       printf("Welcome, admin %s!\n", u.username);
   } else {
       printf("Welcome, %s!\n", u.username);
   }

   return 0;
}

// Main function to handle command-line arguments and initiate the login process
int main(int argc, char *argv[]) {
   if (argc < 2) {
       fprintf(stderr, "Usage: %s <username>\n", argv[0]);
       return 1;
   }

   // Fix: argv[1] is still untrusted user input, but process_login now validates
   // the length before copying it, so unsafe input does not reach a vulnerable copy.
   return process_login(argv[1]);
}
