#include <stdio.h>

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    if (num <= 1) {
        printf("%d not a prime number.\n", num);
    } else {
        int isPrime = 1;

        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                isPrime = 0;
                break;
            }
        }

        if (isPrime) {
            printf("%d prime number.\n", num);
        } else {
            printf("%d not a prime number.\n", num);
        }
    }

    return 0;
}
