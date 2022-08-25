#include <stdio.h>
#include <time.h>
#include <stdlib.h>

void rps(int choice){
    // 1 is rock, 2 is paper, 3 is scissors

    // random is computer's choice
    int random = 1;

    // generate random number from 1 - 3
    srand(time(0));
    random = rand() % 4;

    // determine win, lose, draw and print result
    if (random == 1){
        if (choice == 2) {
            printf("You Win");
        }
        else if (choice == 3) {
            printf("You Lose");
        }
        else {
            printf("Draw");
        }
    }
    if (random == 2){
        if (choice == 3) {
            printf("You Win");
        }
        else if (choice == 1) {
            printf("You Lose");
        }
        else {
            printf("Draw");
        }
    }
    if (random == 3){
        if (choice == 1) {
            printf("You Win");
        }
        else if (choice == 2) {
            printf("You Lose");
        }
        else {
            printf("Draw");
        }
    }
}

int main(){
    // must pass in 1 - 3
    rps(1);
}