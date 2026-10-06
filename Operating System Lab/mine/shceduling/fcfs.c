#include<stdio.h> 

struct  Process{
    int pid;
    int arrival;
    int brust;
    int completion;
    int trunaround;
    int waiting;
};

int main() {
    int n;
    printf("Enter number of processes: ");
    scanf("%d", &n);

    struct Process p[n];

    for(int i = 0; i < n; i++) {
        p[i].pid = i + 1;

        printf("\nProcess P %d\n", p[i].pid);

        printf("Arrival Time: ");
        scanf("%d", &p[i].arrival);

        printf("Brust Time: ");
        scanf("%d", &p[i].brust);
    }

    for(int i = 0; i < n - 1; i++) {
        for(int j = i + 1; j < n; j++) {
            if(p[i].arrival > p[j].arrival) {
                struct Process temp = p[i];
                p[i] = p[j];
                p[j] = temp;
            }
        }
    }

    int current_time = 0;
    float total_waiting = 0;
    float total_turnaround = 0;

    for(int i = 0; i < n; i++) {
        if(current_time < p[i].arrival) {
            current_time = p[i].arrival;
        }

        p[i].completion = current_time + p[i].brust;

        p[i].trunaround = p[i].completion - p[i].arrival;   

        p[i].waiting = p[i].trunaround - p[i].brust;

        current_time = p[i].completion;

        total_waiting += p[i].waiting;
        total_turnaround += p[i].trunaround;
    }

    printf("PID\tAT\tBT\tCT\tTAT\tWT\n");
    printf("--------------------------------------------------\n");

    for (int i = 0; i < n; i++) {
        printf("P%d\t%d\t%d\t%d\t%d\t%d\n",
               p[i].pid,
               p[i].arrival,
               p[i].brust,
               p[i].completion,
               p[i].trunaround,
               p[i].waiting);
    }

    printf("--------------------------------------------------\n");

    printf("Average Waiting Time = %.2f\n",
           total_waiting / n);

    printf("Average Turnaround Time = %.2f\n",
           total_turnaround / n);


    printf("\nGantt Chart:\n");

printf(" ");
for (int i = 0; i < n; i++) {
    printf("--------");
}
printf("\n|");

for (int i = 0; i < n; i++) {
    printf("  P%d   |", p[i].pid);
}

printf("\n ");

for (int i = 0; i < n; i++) {
    printf("--------");
}

printf("\n%d", p[0].arrival);

for (int i = 0; i < n; i++) {
    printf("%8d", p[i].completion);
}

printf("\n");

    return 0;


}