#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <cs50.h>

int main(int argc, string args[]){
    if (argc != 2)
    {
        printf("Usage: ./caesar k\n");

        return 1;
    }


    int key = atoi(args[1]) % 26;
    string plaintext = get_string("plaintext: ");


    printf("ciphertext: ");

    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        if (!(65<=plaintext[i] && plaintext[i]<=90) && !(97<=plaintext[i] && plaintext[i]<=122))
        {
            printf("%c", plaintext[i]);
            continue;
        }

        // Uppercase letter's index has a different offset than the lowercase counterpart in ascii table
        int ascii = isupper(plaintext[i]) ? 65 : 97;

        int pi = plaintext[i] - ascii;
        int ci = (pi + key) % 26;

        printf("%c", ci + ascii);
    }

    printf("\n");
    return 0;

}