/*
* 1. Explain the code below.
* 2. Find and fix the bug(s) in the code below.
* It's okay to use man page or internet search. 
* Language: C
*/
 
 
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
 

// Vulnerable point: username and is_admin are stored next to each other.
// If username overflows, it can overwrite is_admin and turn a normal user into an admin.
typedef struct {
   char username[16];
   int is_admin;
} User;
 
// Function to process user login
void process_login(char *input) {
   User u;
   u.is_admin = 0;

   // Vulnerable point: strcpy does not check the size of u.username.
   // Any input longer than 15 characters plus the null terminator can overflow this buffer.
   strcpy(u.username, input); 

   // Vulnerable point: this admin check depends on memory that can be overwritten by the buffer overflow above.
   if (u.is_admin) {
       printf("Welcome, admin %s!\n", u.username);
   } else {
       printf("Welcome, %s!\n", u.username);
   }
}
 
// Main function to handle command-line arguments and initiate the login process
int main(int argc, char *argv[]) {
   if (argc < 2) { fprintf(stderr, "Usage: %s <username>\n", argv[0]); return 1; }

   // Vulnerable point: argv[1] is untrusted user input and no length check is done before passing it into process_login.
   process_login(argv[1]);
   return 0;
}
