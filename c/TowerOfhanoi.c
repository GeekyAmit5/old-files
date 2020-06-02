#include <stdio.h>
void hanoi(int n, char f, char a, char t);
int moves = 0;
int main()
{
    int n;
    printf("How Many Disks You Want to Move ? ");
    scanf("%d", &n);
    hanoi(n, 'A', 'B', 'C');
    printf("Done!\n");
    printf("Total Moves = %d", moves);
    return 0;
}

void hanoi(int n, char f, char a, char t)
{
    if (n != 0)
    {
        hanoi(n - 1, f, t, a);
        printf("Move a disk from %c to %c\n", f, t);
        moves++;
        hanoi(n - 1, a, f, t);
    }
}
