#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - function that contains an infinite loop
 *
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - Entry point
 *
 * Return: Always 0
 */
int main(void)
{
	int i, pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}

	infinite_while();
	return (0);
}
