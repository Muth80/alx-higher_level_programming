#include "lists.h"

/**
 * print_dlistint - prints all the elements of a dlistint_t list
 * @n: pointer to head node of list
 * Return: number of nodes in the list
 */

size_t print_dlistint(const dlistint_t *n);
{
	size_t count = 0;

	while (n != NULL)
	{
		printf("%d\n", n->n);
		n = n->next;
		count++;
	}

	return (count);
}
